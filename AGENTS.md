# AGENTS.md for CS1060 HW9 Project

## Project Overview

This repository is the home for the CS1060 Homework 9 project work. It currently serves as a team repository for tracking our agent guidance, testing plan, and CI/CD conventions for the project.

## Project Context

- Team: CS1060 Project Team
- Repository: `cs1060-hw9`
- Purpose: document project goals, agent guidance, and testing/CI expectations for homework deliverables.
- Scope: the repository currently contains documentation metadata; application code and infrastructure may be added later as part of homework implementation.

## Agent Guidance

This file is intended to give an AI assistant a stable context for working in this repository, including how to approach tests, CI, and not modifying existing test cases unless requested.

### Goals for the agent

- Respect the repository structure and existing files.
- Add documentation or code only when it aligns with explicit homework requirements.
- Avoid changing tests unless the user explicitly asks for test updates.
- Preserve team conventions and tag feature work clearly when committing.

### Agent Behavior

- Ask for clarification if a requested task is ambiguous.
- Prefer documentation and small changes when repository contents are minimal.
- Focus on generating clear, maintainable contributions.

## Testing Instructions

### Continuous Integration Plan

- Use GitHub Actions to run repository tests on every commit and pull request.
- Only deploy to production when the `main` branch build passes successfully.
- For feature branches and pull requests, generate a preview deployment or report build status without deploying to production.
- The CI plan should include:
  - install dependencies
  - run linting/static analysis
  - execute automated tests
  - report results back to GitHub
  - only deploy if all checks pass on `main`

### How to Run Tests

- Identify the repository's test command from `package.json` or equivalent configuration.
- Run the test suite locally first, for example:
  - `npm test`
  - `pytest`
  - `cargo test`
- If there is no test framework currently installed, update the repository with one before adding feature code.

### How to Run Linters / Static Analysis

- Determine the appropriate toolchain for the project language.
- Example commands:
  - `npm run lint`
  - `flake8 .`
  - `eslint .`
- Use the same linting commands in CI so the local and remote workflows match.

### When to Update Tests

- Update or add tests whenever a new feature is implemented.
- Update tests when a bug fix changes expected behavior.
- Do not change existing tests unless explicitly requested by the user or when the behavior of the code is intentionally changed.

### Test Change Policy

- Existing tests are treated as the source of truth unless the user requests a behavior change.
- If a failing test reveals a bug in implementation, fix the code rather than modify the test, unless the test is outdated or incorrect.
- Document any test updates clearly in the commit message.

## Notes for Contributors

- Use clear branch names for HW9 work, such as `lawrence-matrix-hw9`.
- Include `HW9` and a ticket identifier in commit messages, for example: `HW9 TASK-XX: add AGENTS.md and CI guidance`.
- Keep documentation readable and maintain a consistent project context.
- Ensure any external links (Vercel, Google Docs, project index) are added to the shared submission template, not to this repository file unless explicitly requested.
