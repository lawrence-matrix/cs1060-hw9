# HW9 Submission Template Guide

This document outlines the structure and links for the CS1060 HW9 submission.

## Instructions
1. Copy the Google Template from: https://docs.google.com/document/d/1LptXTTlV-C2EZfThC3vWdNihzyRcCTYbWlKzQ_x4OZA/edit
2. Use "File → Make a copy" to create your own copy
3. Fill in the following sections with links and information from your work:

---

## 1. Retrospective (5 points)
**Link to retrospective in project index:** [Add link after completing]

**Summary:** Discuss candidly how HW8 work went, time spent by team members, and merge conflict experiences.

---

## 2. Peer Feedback (5 points)
**Link to peer feedback document:** [Add link to shared Google Doc after creating]

**Summary:** Collected feedback from peers during the 2025-10-30 lecture.

---

## 3. AGENTS.md (10 points)
**Repository:** cs1060-hw9
**Link to AGENTS.md:** https://github.com/lawrence-matrix/cs1060-hw9/blob/lawrence-matrix-hw9/AGENTS.md

**Completed:**
- ✓ General AGENTS.md with project context and agent guidance (5 points)
- ✓ Testing instructions section with CI plan, test commands, linting, and test update policy (5 points)

---

## 4. Implementation (30 points)
**Feature Branch:** `lawrence-matrix-hw9`
**Repository:** https://github.com/lawrence-matrix/cs1060-hw9
**Branch Commit:** https://github.com/lawrence-matrix/cs1060-hw9/commit/86894de82a784e6577a95c5b4494fd106b5dabbb

**Tickets Implemented:**
- TASK-1: Matrix utility library (data structures and operations)
  - Includes comprehensive unit tests
  - Committed with "HW9" prefix
- TASK-2: CI workflow and deployment support
  - Added GitHub Actions workflow and Vercel deployment steps
- TASK-3: Project documentation and submission guidance
  - Added AGENTS.md, README, retrospective, peer feedback, and submission template

---

## 5. CI/CD Part 1 (10 points)
**Repository:** https://github.com/lawrence-matrix/cs1060-hw9
**GitHub Actions Link:** https://github.com/lawrence-matrix/cs1060-hw9/actions
**Vercel Preview URL:** [Requires Vercel secrets and project configuration]
**Vercel Production URL:** [Requires Vercel secrets and project configuration]

**Completed:**
- [x] Added Vercel deployment step to CI workflow
- [x] Configured deployable static app with `public/index.html`
- [x] Added Vercel project config in `vercel.json`
- [ ] Set Vercel GitHub secrets in repo
- [ ] Confirm actual preview and production URLs after deployment

**Completed:**
- [ ] GitHub secrets configured (VERCEL_TOKEN, VERCEL_ORG_ID, VERCEL_PROJECT_ID)
- [ ] Failing tests fixed
- [ ] CI workflow configured to deploy to production only when tests pass
- [ ] Workflow does NOT deploy to production when tests fail on main
- [ ] Merge to main triggers production deployment

---

## Shared Repository Access
- [ ] cs1060-hw9 shared with: ssayer-lgtm, kingshukkundu
- [ ] faleproxy shared with: ssayer-lgtm, kingshukkundu
