---
hero:
  title: GitHub DocS Core
  subtitle: Authoritative, developer-focused documentation for the GitHub REST API.
  link:
    text: Quick Start
    url: quickstart/
---

Authoritative, developer-focused documentation for 288+ GitHub REST API endpoints. All content is generated directly from the Postman collection and repository source — nothing is speculated or invented.

## Documentation Structure

This site follows the [Diátaxis](https://diataxis.fr/) framework. Content is divided into four distinct categories, each serving a different purpose:

| Section | Purpose | Start Here If... |
| --- | --- | --- |
| [Quick Start](quickstart.md) | First API call in under 10 minutes | You are new to the GitHub API |
| [Tutorials](tutorials/index.md) | Learning through doing | You want to understand how the API works |
| [How-to Guides](how-to/index.md) | Recipes for specific tasks | You know what you want to accomplish |
| [Explanations](explanations/index.md) | Conceptual understanding | You want to know why, not just how |
| [API Reference](api-reference/repos.md) | Complete endpoint catalogue | You need exact parameter and schema details |

---

## Core Design Principles

**Traceable**
: Every statement is verifiable against a source artifact — the Postman collection, the repository, or a live API response. No speculated functionality is documented.

**Deterministic**
: Documentation is generated through defined, repeatable processes via the Automation Tier. The same inputs always produce the same outputs.

**Developer-Focused**
: Optimized for operational clarity. Endpoints include cURL, Python, and JavaScript examples. Parameters link to specific schema definitions. Error codes map to verified API responses.

---

## System Components

**Expert Modules** (`expert-modules/`)
: Logical capability manifests. Define what content to generate and how to structure it. The `dx-docs-expert` module implements the Diátaxis framework for this site.

**Automation Processors** (`automation-tier/`)
: Deterministic Python scripts. Execute file generation, schema extraction, auditing, and deployment. No semantic decisions are made here.

**MkDocs Material**
: High-fidelity documentation theme. Provides tabbed code examples, admonitions, full-text search, and dark mode support.

---

> [!NOTE]
> This documentation is automatically synchronized with the Postman collection source of truth. When the collection changes, the processors regenerate affected pages and validate navigation integrity before deployment.
