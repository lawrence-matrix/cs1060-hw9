# cs1060-hw9

This repository contains CS1060 HW9 project work.

## Contents

- `AGENTS.md` — AI assistant guidance and testing instructions
- `src/matrix.py` — matrix library implementation
- `tests/test_matrix.py` — pytest coverage for matrix utilities
- `public/index.html` — static homepage for deployment
- `.github/workflows/ci.yml` — CI pipeline with Vercel deployment support
- `vercel.json` — Vercel static deployment configuration

## How to deploy

1. Configure GitHub Actions secrets:
   - `VERCEL_TOKEN`
   - `VERCEL_ORG_ID`
   - `VERCEL_PROJECT_ID`
2. Push to a feature branch to trigger preview deployment.
3. Merge to `main` to trigger production deployment.

## Local test commands

- `python -m pip install -r requirements.txt`
- `python -m pytest tests/ -v --tb=short`
