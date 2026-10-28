import pygame
import random
from pathlib import Path
from .player import Player
from .enemy import EnemyGrid
from .bullet import Bullet

# Game Engine

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 60, 60)


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Load sound effects once. Audio is optional so the game still
        # works if the mixer or sound files are unavailable.
        self._sound_enabled = False
        self.player_fire_sound = None
        self.enemy_destroyed_sound = None
        self.game_over_sound = None
        self._load_sounds()

        self.font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 56, bold=True)
        self.message_font = pygame.font.SysFont("Arial", 28)

        # Game states: playing -> game_over -> difficulty_select -> playing
        self.state = "playing"
        self.game_over = False
        self.difficulty = "Medium"

        self._start_new_game(self.difficulty)

    def _load_sounds(self):
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()

            sound_dir = Path(__file__).resolve().parent.parent / "assets" / "sounds"

            self.player_fire_sound = pygame.mixer.Sound(
                sound_dir / "player_fire.wav"
            )
            self.enemy_destroyed_sound = pygame.mixer.Sound(
                sound_dir / "enemy_destroyed.wav"
            )
            self.game_over_sound = pygame.mixer.Sound(
                sound_dir / "game_over.wav"
            )
            self._sound_enabled = True
        except (pygame.error, OSError):
            # Audio is optional; gameplay should continue without it.
            self._sound_enabled = False

    def _play_sound(self, sound):
        if self._sound_enabled and sound is not None:
            try:
                sound.play()
            except pygame.error:
                pass

    def _difficulty_settings(self, difficulty):
        settings = {
            "Easy": {"speed": 1.0, "fire_chance": 0.005},
            "Medium": {"speed": 1.5, "fire_chance": 0.01},
            "Hard": {"speed": 2.5, "fire_chance": 0.02},
        }
        return settings[difficulty]

    def _start_new_game(self, difficulty):
        # Create a completely fresh game state.
        settings = self._difficulty_settings(difficulty)

        self.difficulty = difficulty
        self.state = "playing"
        self.game_over = False

        self.player = Player(self.width // 2 - 20, self.height - 50, 40, 20)
        self.enemy_grid = EnemyGrid(self.width, speed=settings["speed"])

        self.player_bullets = []
        self.enemy_bullets = []
        self._shoot_cooldown = 0
        self.enemy_fire_chance = settings["fire_chance"]
        self.score = 0

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        if self.state == "game_over":
            # P = play again, ESC = exit.
            if event.key == pygame.K_p:
                self.state = "difficulty_select"
            elif event.key == pygame.K_ESCAPE:
                return "quit"
            return None

        if self.state == "difficulty_select":
            if event.key == pygame.K_e:
                self._start_new_game("Easy")
            elif event.key == pygame.K_m:
                self._start_new_game("Medium")
            elif event.key == pygame.K_h:
                self._start_new_game("Hard")
            elif event.key == pygame.K_ESCAPE:
                return "quit"
            return None

        # Normal gameplay input.
        if event.key == pygame.K_SPACE and self._shoot_cooldown <= 0:
            bullet_x = self.player.center_x() - 2
            self.player_bullets.append(
                Bullet(bullet_x, self.player.y, direction=-1)
            )
            self._play_sound(self.player_fire_sound)
            self._shoot_cooldown = 15

        return None

    def handle_input(self):
        # Player movement is allowed only during normal gameplay.
        if self.state != "playing":
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-self.player.speed, self.width)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(self.player.speed, self.width)

    def update(self):
        # No gameplay updates are performed outside the playing state.
        if self.state != "playing":
            return

        if self._shoot_cooldown > 0:
            self._shoot_cooldown -= 1

        self.enemy_grid.move()

        for enemy in self.enemy_grid.alive_enemies():
            if random.random() < self.enemy_fire_chance:
                bullet_x = enemy.x + enemy.width // 2
                self.enemy_bullets.append(
                    Bullet(
                        bullet_x,
                        enemy.y + enemy.height,
                        direction=1
                    )
                )

        for bullet in self.player_bullets:
            bullet.move()
        for bullet in self.enemy_bullets:
            bullet.move()

        self.player_bullets = [
            b for b in self.player_bullets
            if not b.off_screen(self.height)
        ]
        self.enemy_bullets = [
            b for b in self.enemy_bullets
            if not b.off_screen(self.height)
        ]

        # Resolve player bullet collisions without modifying the list
        # while iterating over it. Each bullet can destroy at most one enemy.
        bullets_to_remove = set()

        for bullet in self.player_bullets:
            for enemy in self.enemy_grid.alive_enemies():
                if bullet in bullets_to_remove:
                    break

                if bullet.rect().colliderect(enemy.rect()):
                    enemy.alive = False
                    bullets_to_remove.add(bullet)
                    self.score += 1
                    self._play_sound(self.enemy_destroyed_sound)
                    break

        if bullets_to_remove:
            self.player_bullets = [
                bullet for bullet in self.player_bullets
                if bullet not in bullets_to_remove
            ]

        # Either condition ends the current game.
        for bullet in self.enemy_bullets:
            if bullet.rect().colliderect(self.player.rect()):
                self._set_game_over()
                break

        if self.enemy_grid.reached_bottom(self.player.y):
            self._set_game_over()

    def _set_game_over(self):
        # Only play the sound when transitioning into game over.
        if self.state != "game_over":
            self._play_sound(self.game_over_sound)

        self.game_over = True
        self.state = "game_over"

    def restart(self):
        # Keep this method for compatibility with the previous version.
        # A restart now goes through difficulty selection.
        self.state = "difficulty_select"

    def render(self, screen):
        if self.state == "playing":
            self._render_game(screen)
        elif self.state == "game_over":
            self._render_game_over(screen)
        elif self.state == "difficulty_select":
            self._render_difficulty_select(screen)

    def _render_game(self, screen):
        pygame.draw.rect(screen, GREEN, self.player.rect())

        for enemy in self.enemy_grid.alive_enemies():
            pygame.draw.rect(screen, WHITE, enemy.rect())

        for bullet in self.player_bullets:
            pygame.draw.rect(screen, WHITE, bullet.rect())

        for bullet in self.enemy_bullets:
            pygame.draw.rect(screen, RED, bullet.rect())

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    def _draw_overlay(self, screen):
        overlay = pygame.Surface((self.width, self.height))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(220)
        screen.blit(overlay, (0, 0))

    def _render_game_over(self, screen):
        self._draw_overlay(screen)

        game_over_text = self.title_font.render("GAME OVER", True, RED)
        score_text = self.message_font.render(
            f"Final Score: {self.score}", True, WHITE
        )
        play_text = self.message_font.render(
            "P - Play Again", True, WHITE
        )
        exit_text = self.message_font.render(
            "ESC - Exit", True, WHITE
        )

        screen.blit(
            game_over_text,
            game_over_text.get_rect(
                center=(self.width // 2, self.height // 2 - 120)
            ),
        )
        screen.blit(
            score_text,
            score_text.get_rect(
                center=(self.width // 2, self.height // 2 - 40)
            ),
        )
        screen.blit(
            play_text,
            play_text.get_rect(
                center=(self.width // 2, self.height // 2 + 40)
            ),
        )
        screen.blit(
            exit_text,
            exit_text.get_rect(
                center=(self.width // 2, self.height // 2 + 90)
            ),
        )

    def _render_difficulty_select(self, screen):
        self._draw_overlay(screen)

        title_text = self.title_font.render(
            "SELECT DIFFICULTY", True, WHITE
        )
        easy_text = self.message_font.render(
            "E - EASY", True, WHITE
        )
        medium_text = self.message_font.render(
            "M - MEDIUM", True, WHITE
        )
        hard_text = self.message_font.render(
            "H - HARD", True, WHITE
        )
        exit_text = self.message_font.render(
            "ESC - Exit", True, WHITE
        )

        screen.blit(
            title_text,
            title_text.get_rect(
                center=(self.width // 2, self.height // 2 - 130)
            ),
        )
        screen.blit(
            easy_text,
            easy_text.get_rect(
                center=(self.width // 2, self.height // 2 - 40)
            ),
        )
        screen.blit(
            medium_text,
            medium_text.get_rect(
                center=(self.width // 2, self.height // 2 + 10)
            ),
        )
        screen.blit(
            hard_text,
            hard_text.get_rect(
                center=(self.width // 2, self.height // 2 + 60)
            ),
        )
        screen.blit(
            exit_text,
            exit_text.get_rect(
                center=(self.width // 2, self.height // 2 + 120)
            ),
        )
