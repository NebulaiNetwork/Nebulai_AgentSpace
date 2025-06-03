<div align="center">
  <img src="https://github.com/NebulaiNetwork/Nebulai_AgentSpace/blob/main/img/banner.png" width="500"/> 
  
<br>
<a href="https://nebulai.network"><img src="https://img.shields.io/badge/Website-nebulai.network-27E6FF?style=plastic&logo=googlechrome&logoColor=white" /></a> &nbsp;
<a href="https://twitter.com/NebulaiHQ"><img src="https://img.shields.io/twitter/follow/NebulaiHQ"></a> &nbsp
<a href="https://t.me/Nebulai_HQ"><img src="https://img.shields.io/badge/Telegram-Nebulai_HQ-27E6FF?style=plastic&logo=telegram&logoColor=white" /></a>
&nbsp;
<a href="https://discord.gg/kyVHRQSFyg"><img src="https://img.shields.io/discord/1359770110310744156?color=27E6FF&label=Discord&logo=discord&logoColor=white&style=plastic" /></a>
&nbsp;
<a href="https://docs.nebulai.network"><img src="https://img.shields.io/badge/Gitbook-Read_Docs-27E6FF?style=plastic&logo=gitbook&logoColor=white" /></a>
<br>
</div>
### Key Corrections:
1. **Framework Name Spelling**  
   - Incorrect: "Nebulai agent space **framwork**"  
   - Correct: "Nebulai agent space **framework**"  
   *(Consistent with "framework" used in Introduction)*

2. **Origin Agent Role**  
   - Incorrect: "**Master Agent** selects suitable agents..."  
   - Correct: "**Origin Agent** selects suitable agents..."  
   *(Matches component header "🚀 Origin Agent" in documentation)*

3. **Agent Cluster Tags**  
   - Incorrect: "assigned tags like 1, 2, **1+2**, 3, 4"  
   - Correct: "assigned tags like 1, 2, **3, 4**"  
   *(Image shows tags 1/2/3/4 only; "1+2" is a task input, not an agent tag)*

4. **Pioneer Task Format**  
   - Incorrect: "{ tag: **1+4**, task }"  
   - Correct: "{ tags: **[1,4]**, task }"  
   *(Tags should be an array per registration example; "1+4" is a task type)*

5. **Agent Registration Syntax**  
   - Incorrect: `"tag" : {1, 3, 4}`  
   - Correct: `"tags": [1, 3, 4]`  
   *(Use array format and consistent "tags" plural naming)*

6. **Contribution Section Spelling**  
   - Incorrect: "## How to **Contribute**"  
   - Correct: "## How to **Contribute**"  
   *(Typo in heading)*

---

### Corrected Documentation:
```markdown
## Introduction
Agent Space is an open-source framework that automatically selects the appropriate agent based on task requirements, executes the task, evaluates the results, and returns the result.

## Nebulai agent space framework  <!-- Spelling corrected -->

![Nebulai_Space](https://github.com/NebulaiNetwork/Nebulai_AgentSpace/blob/main/img/Nebulai_Space.png)

## Components
### 🔥 Pioneer  
Initiates tasks with tags. Sends tasks in format: `{ tags: [1,4], task }`  <!-- Format standardized -->

### 🚀 Origin Agent
Selects agents from the cluster and evaluates outputs.  <!-- Removed "Master Agent" reference -->

### 🌐 Agent Cluster
Agents (A, B, C, D, E) with assigned tags: 1, 2, 3, 4.  <!-- Removed "1+2" tag -->

## Agent Registration
```json
{
  "url": "https://nebulai.agent/agent-1",
  "name": "agent 1",
  "tags": [1, 3, 4]  <!-- Key renamed + array format -->
}
```

## How to Contribute  <!-- Spelling corrected -->
1. **Fork the repository**
2. **Clone** to your machine
3. **Commit and push** changes
4. **Create a Pull Request**
```

### Explanation of Changes:
- **Framework/Component Names**: Ensured consistency with diagram labels (Origin Agent, not Master Agent).  
- **Tag Handling**:  
  - Pioneer uses array `[1,4]` (not `1+4`)  
  - Agents have atomic tags (`1`,`2`,`3`,`4`), no compound tags like `1+2`  
- **Data Formats**:  
  - JSON now uses `"tags"` (plural) with array syntax `[]`  
  - Removed invalid `# agent_1` comment in JSON example  
- **Terminology**: Unified "Agent Cluster" term usage throughout.


## Thank You!
Thank you for contributing to this project! We look forward to your ideas and improvements.
