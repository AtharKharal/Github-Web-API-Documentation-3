# Practitioner: The Flow Designer

## Goal
Create logical, step-by-step developer journey workflows with 1:1 documentation fidelity.

## Logic Overview
1. **Flow Identification**: Synthesize related API endpoints into a functional workflow (e.g., "Authentication -> Get Profile -> Update Data").
2. **Step Documentation**: For each step, create:
    - **Step Number**: Numeric sequence.
    - **Title**: Clear, action-oriented heading.
    - **Narrative**: Brief, operational explanation.
    - **Code Block**: Snippet for the key API call.
    - **Mermaid Diagram**: Visualization of the sequence.

## Apparatus Mapping
- **Script**: `apparatus/generate_workflows.py`
- **Input**: YAML flow definition.

## Templates
- **Primary**: `practitioners/lib/templates/workflow_step.md.j2`
- **Mermaid**: `practitioners/lib/templates/mermaid_flow.md.j2`

## Standards Compliance
- Must use Mermaid syntax for visual state.
- Must include "Recipe" admonitions.
