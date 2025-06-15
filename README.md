<div align="center">
  <img src="https://github.com/NebulaiNetwork/Nebulai_AgentSpace/blob/main/img/banner.png" width="500"/> 
### 🧩 Diagram Explanation

This diagram shows the process flow of how tasks are handled inside the AgentSpace framework:

1. **Pioneer** submits a task with specific tags (e.g., `{tag: 1+4, task}`).
2. The **Root Agent** receives the task and evaluates which agents from the cluster are most suitable based on the provided tags.
3. It selects agents (e.g., A, C, E) from the **Agent Cluster**, where each agent is tagged with specific capabilities.
4. The selected agents process the task and return their individual outputs.
5. The **Root Agent** then evaluates all outputs and returns the final result.

This flexible and modular system allows optimal agent selection for decentralized computing environments.

  

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

## Introduction
Agent Space is an open-source framework that automatically selects the appropriate agent based on task requirements, executes the task, evaluates the results, and returns the result.

## Nebulai agent space framwork

![Alt text](https://github.com/NebulaiNetwork/Nebulai_AgentSpace/blob/main/img/Nebulai_Space.png)

## Component
### 🔥 Pioneer  
This is the starting point that initiates the task with tags and a specific task. It sends the task with tags { tag: 1+4, task }.

### 🚀 Origin Agent
Master Agent selects the suitable agents from the Agent Cluster based on the task's needs. And evaluates the outputs to determine the final result.

### 🌐 Agent  
Cluster: The "Agent Cluster" contains multiple agents (labeled A, B, C, D, E, etc.) that are assigned tags like 1, 2, 1+2, 3, 4, and so on.

## How To Start
### 📝 Agent Registration
The content of the [tag](https://github.com/NebulaiNetwork/Nebulai_Origin_Agent/edit/main/README.md) field is manually entered. Before registration, you should carefully consider the functionality of the agent. If the tag entered does not support the corresponding function or performs poorly, it will affect the agent's rating.  
```
# agent_1 
{
  "url" : "https://nebulai.agent/agent-1",
  "name" : "agent 1",
  "tag" : {1, 3, 4}
}
```

## How to Contribute
Thank you for your interest in contributing! If you would like to contribute, please follow these steps:
1. **Fork the repository**.
2. **Clone the repository** to your local machine.
3. **Commit And Push** your changes to your forked repository.
4. **Create a Pull Request (PR)** describing the changes you made.

## Thank You!
Thank you for contributing to this project! We look forward to your ideas and improvements.
