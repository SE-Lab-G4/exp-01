# Experimental IoT Platform (`exp-01`)

## Overview
This project is part of an IoT research and development experiment. The repository follows a structured branching strategy to ensure modular and efficient development.

## Branching Strategy
- `main`: The stable, production-ready branch (protected).
- `develop`: The staging branch where new features are merged before reaching `main`.
- `feature/*`: Dedicated branches for each module.

## Branch Protection Rules
To ensure stable and high-quality code, we have set up the following branch protection rules for `main`:
- **Pull Requests are Required**: No direct commits to `main` are allowed. All changes must go through pull requests.
- **Review Approval Required**: At least one team member must approve before merging.
- **Force Push is Disabled**: Prevents rewriting commit history in `main`.
- **Branch Deletion is Restricted**: `main` cannot be accidentally deleted.
- **CI/CD Integration (Upcoming)**: Automated tests and checks will be required before merging (to be configured later).

## Contribution Workflow
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_ORG/exp-01.git
   cd exp-01

