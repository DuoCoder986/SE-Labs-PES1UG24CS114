Lab 6 — Code and Branch Coverage

Application: `visa_application.py` (provided module; unchanged).

Test suites:
- `CodeCoverageTest_52_visa_application.py` — tests for statement/code coverage.
- `BranchCoverageTest_52_visa_application.py` — tests for decision outcomes and branch coverage.

Install dependencies:

```powershell
python -m pip install pytest coverage
```

Run code coverage:

```powershell
python -m coverage erase
python -m coverage run --source=visa_application -m pytest -v CodeCoverageTest_52_visa_application.py
python -m coverage report -m
```

Run branch coverage:

```powershell
python -m coverage erase
python -m coverage run --branch --source=visa_application -m pytest -v BranchCoverageTest_52_visa_application.py
python -m coverage report -m
```

Verified results on Python 3.12.10: code coverage 100% (14 tests passed; 37 statements, none missing); branch coverage 100% (27 tests passed; 37 statements, 26 branches, zero partial branches).

Terminal evidence is in `evidence/`. The `.coverage` database and Python caches are intentionally excluded.

The lab handout requires two separate commits: one for the code-coverage test and evidence, and one for the branch-coverage test and evidence.
