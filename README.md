# Grade Tracker

A small Python library that calculates student averages, converts them to letter grades,
loads/saves student records as JSON, and prints class reports.

Used for **CSCN73010 Software Quality III – Assignment 3 (SonarQube Cloud static analysis)**.

| Item | Value |
|---|---|
| Language | Python 3.12 |
| Test framework | pytest (+ pytest-cov for coverage) |
| Baseline version | 1.0.0 (git tag `v1.0.0-baseline`) |
| CI | GitHub Actions → SonarQube Cloud |

## Run locally

```bash
python -m pip install -r requirements-dev.txt
pytest --cov=src --cov-report=xml:coverage.xml --cov-report=term
```

## Project layout

```
src/gradetracker/   application code (grades, storage, report)
tests/              pytest unit tests
data/               sample student records
```
