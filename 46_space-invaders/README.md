# Space Invaders Game

This project is a terminal-based Space Invaders clone using **Pygame**. It introduces students to interactive game design using object-oriented principles and real-time graphical rendering.

---

## What’s Provided

A partially working version of a Space Invaders game with:

- A player-controlled ship that moves and shoots
- A grid of enemies that marches side to side and drops down at the edges
- Enemies that occasionally return fire
- Score display

You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Clone the repo or download the project folder.
2. Make sure you have Python 3.10+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

---

## LLM Chat Used

All four tasks were completed with **ChatGPT** as a debugging and pair-programming partner. The complete chat history is here:

**ChatGPT conversation:** [https://chatgpt.com/share/6ac6083c-52d0-83ee-b139-0ded1cc79f26](https://chatgpt.com/share/6ac6083c-52d0-83ee-b139-0ded1cc79f26)

The exact prompt used for each task is listed under that task below.

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Refine Collision Detection

> Bullets sometimes pass straight through enemies without registering a hit, especially when firing rapidly or when two enemies are hit close together. Investigate and enhance collision accuracy.

**Prompt used:**

```text
You are working on the existing Space Invaders Pygame project.
TASK 1: REFINE COLLISION DETECTION
The current game has a collision-detection bug where player bullets can sometimes pass through enemies without registering a hit, especially when bullets are fired rapidly or multiple collisions occur close together.
Analyze the existing collision implementation and fix it properly.
Requirements:
1. Identify why the current collision detection can skip bullets/enemies.
2. Do NOT remove elements from a list while directly iterating over that same list.
3. Make collision handling reliable when multiple bullets/enemies are present in the same frame.
4. A player bullet should destroy at most one enemy.
5. A destroyed enemy must no longer participate in future collisions.
6. A successful hit must increase the score exactly once.
7. Bullets that do not hit anything should continue moving normally.
8. Preserve the existing player movement, enemy movement, enemy firing, rendering, and game architecture.
9. Do not rewrite the entire project. Make the smallest clean changes necessary.
10. Keep the code understandable for a 3rd-year computer science student.
After making the changes, explain:
- what caused the bug,
- what you changed,
- why the new implementation does not skip collisions,
- and which files were modified.
```


### Task 2: Implement Game Over Condition

> Add a screen that displays the final score once the player is hit or the enemies reach the bottom of the screen, then gracefully waits for input instead of just printing to the console.

**Prompt used:**

```text
You are working on the existing Space Invaders Pygame project.
TASK 2: IMPLEMENT A PROPER GAME OVER CONDITION AND SCREEN
The current project sets game_over = True when the player is hit by an enemy bullet or when enemies reach the player's area, but it only prints the final score to the console.
Replace this behavior with a proper in-game Game Over screen.
Requirements:
1. The game must end when:
- an enemy bullet hits the player, OR
- the enemy grid reaches the bottom/player boundary.
2. Once game_over becomes True:
- stop normal gameplay updates,
- stop player movement,
- stop enemy movement,
- stop spawning/firing new enemy bullets,
- stop accepting normal shooting input.
3. Display a clear Game Over screen inside the Pygame window.
4. Display:
- "GAME OVER"
- the final score
- a message telling the player how to continue/exit.
5. The final score must remain visible and must not change after game over.
6. Do not rely on console print statements as the user-facing game-over behavior.
7. The game window must remain open instead of immediately closing.
8. Handle keyboard input cleanly so the user can exit or continue according to the existing project requirements.
9. Preserve the existing game architecture and avoid rewriting unrelated classes.
10. Keep the implementation simple and readable.
After making the changes, explain:
- how the game-over state works,
- how gameplay is frozen,
- how the screen is rendered,
- and which files were modified.
```



### Task 3: Add Replay Option

> After Game Over, allow the user to play again by choosing a difficulty (Easy, Medium, or Hard enemy speed/fire rate), or exit.

**Prompt used:**

```text
You are working on the existing Space Invaders Pygame project.
TASK 3: ADD A REPLAY OPTION WITH DIFFICULTY SELECTION
After Game Over, allow the player to choose whether to:
1. Play again
2. Exit
If the player chooses to play again, display a difficulty-selection screen with:
- EASY
- MEDIUM
- HARD
Difficulty must affect the enemy behavior.
Requirements:
1. The game-over state should transition to a replay/difficulty-selection state rather than closing the game.
2. On Game Over, display the final score.
3. Provide clear keyboard controls for selecting:
- Play Again
- Exit
4. When Play Again is selected, allow the player to select:
- Easy
- Medium
- Hard
5. Difficulty should affect at least enemy movement speed and enemy firing rate.
6. Suggested behavior:
- Easy: slower enemies and lower firing probability
- Medium: current/default behavior
- Hard: faster enemies and higher firing probability
7. Starting a new game must completely reset:
- player position,
- player bullets,
- enemy bullets,
- enemy grid,
- score,
- shooting cooldown,
- game_over state,
- any game-over/replay flags.
8. The previous game's state must not leak into the new game.
9. Keep the existing classes and architecture where possible.
10. Do not create unnecessary dependencies.
11. Make the implementation easy to understand and maintain.
12. The normal gameplay controls should continue to work after restarting.
After making the changes, explain:
- how the game states are organized,
- how difficulty is represented,
- how a new game is reset,
- what parameters change between Easy/Medium/Hard,
- and which files were modified.
```



### Task 4: Add Sound Feedback

> Add basic sound effects for firing, an enemy being destroyed, and the game-over moment.

**Prompt used:**

```text
You are working on the existing Space Invaders Pygame project.
TASK 4: ADD SOUND FEEDBACK
Add basic sound effects to improve the gameplay experience.
The game must provide sound feedback for:
1. Player firing a bullet
2. Enemy being destroyed
3. Game Over
Requirements:
1. Use Pygame's built-in mixer/audio functionality.
2. Add a sound when the player fires.
3. Add a sound when an enemy is successfully destroyed.
4. Add a sound when Game Over occurs.
5. A sound should play only when the corresponding event actually occurs.
6. The Game Over sound must not repeatedly play every frame.
7. Do not block or freeze the game while playing sounds.
8. Handle missing sound files gracefully rather than crashing the game.
9. Store sound assets in a clear location, such as:
assets/sounds/
10. Update the project structure/documentation if new assets are required.
11. Keep the current gameplay behavior unchanged apart from adding audio.
12. Do not rewrite unrelated gameplay logic.
If appropriate, initialize the mixer safely and load the sounds once instead of repeatedly loading them during the game loop.
After making the changes, explain:
- where the sounds are loaded,
- when each sound is triggered,
- how repeated Game Over sounds are prevented,
- how missing audio files are handled,
- and which files were modified/added.
```


---

## Expected Behavior

- Smooth player movement using `Left`/`Right` or `A`/`D`, and shooting with `Space`
- Enemy grid marches side to side and drops down whenever it reaches a screen edge
- Enemies occasionally fire back at the player
- Score increases each time an enemy is destroyed
- Game ends when the player is hit by an enemy bullet or the enemy grid reaches the bottom of the screen

---

## Folder Structure

```
space-invaders-main/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── player.py
│   ├── enemy.py
│   └── bullet.py
├── assets/
│   └── sounds/
│       ├── player_fire.wav
│       ├── enemy_destroyed.wav
│       └── game_over.wav
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history: [https://chatgpt.com/share/6ac6083c-52d0-83ee-b139-0ded1cc79f26](https://chatgpt.com/share/6ac6083c-52d0-83ee-b139-0ded1cc79f26)
