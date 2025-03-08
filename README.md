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


## Feature Branches

To ensure modular and structured development, we have created dedicated feature branches for different modules:

- **`feature/iot-sensors`**:  
  This branch is used for developing the **IoT sensor module**. It will handle data collection, processing, and communication with the backend.

- **`feature/web-dashboard`**:  
  This branch is used for developing the **web dashboard**. It will be responsible for visualizing IoT data and providing user interaction.

### Contribution Workflow

1. **Switch to the latest `develop` branch**:
   ```bash
   git checkout develop
   git pull origin develop
   ```
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature develop
   ```
3. **Push the branch to GitHub**:
   ```bash
   git push -u origin feature/your-feature
   ```
4. **Submit a Pull Request** to merge your changes into `develop`.


## Commit Message Guidelines

To maintain a clear and structured commit history, all commit messages should follow this format:

```
[Type] Short, descriptive message

Description of changes (if needed)
Issue reference: #IssueNumber
```

### **Commit Types:**
- **feat**: Adding a new feature  
- **fix**: Fixing a bug  
- **docs**: Documentation updates  
- **style**: Code formatting (no logic changes)  
- **refactor**: Code restructuring without changing functionality  
- **test**: Adding or updating tests  
- **chore**: Maintenance tasks (build, CI/CD, dependencies, etc.)  

### **Example Commit Messages:**
```bash
git commit -m "[feat] Implement IoT sensor data streaming"

git commit -m "[fix] Resolve memory leak in dashboard module"

git commit -m "[docs] Update README with commit standards"
```

