# Agent Registration Format

Each agent should register with the following structure:

```json
{
  "url": "https://agentspace.nebulai.io/agents/agent-1",
  "name": "Agent 1",
  "tag": [1, 3, 4]
}


🔖 Tag System
Each tag represents a skill or capability.

Example:

1 – Data Analysis

3 – Natural Language Processing

4 – Image Generation

❗ Rules
url: Must be a valid HTTPS endpoint.

name: Max 64 characters.

tag: Must be an array of integers between 1–99.