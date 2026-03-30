# Practitioner: The Deployment Specialist

## Goal
Automate the build and deployment of the high-fidelity documentation website to GitHub Pages, ensuring consistency and high performance.

## Logic Overview
1. **Repository State**: Validate that the current workspace has an initialized Git repository with a `main` branch.
2. **Build Execution**: Run MkDocs build to generate the static `site/` directory.
3. **CI/CD Integration**: Generate a GitHub Actions workflow using Jinja2 templates.
4. **Publishing**: Handle the transition from local build to public URL via `mkdocs gh-deploy`.

## Apparatus Mapping
- **Script**: `apparatus/deploy_to_gh_pages.py`
- **Input**: None (uses workspace configuration).
- **Execution**: Automates the Git stages (add, commit, push) and MkDocs deployment.

## Templates
- **Primary**: `practitioners/lib/templates/gh_actions_deploy.yml.j2`

## Standards Compliance
- Must use zero-downtime deployment patterns.
- Must ensure that `.gitignore` prevents sensitive credentials from being committed.
- Must verify that the deployment branch is managed consistently.
