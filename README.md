<div align="center">
  <img src="https://github.com/NebulaiNetwork/Nebulai_AgentSpace/blob/main/img/banner.png" width="600"/>  
  <br><br>
  <a href="https://nebulai.network">
    <img src="https://img.shields.io/badge/Website-nebulai.network-27E6FF?style=plastic&logo=googlechrome&logoColor=white" />
  </a> &nbsp;
  <a href="https://twitter.com/NebulaiHQ">
    <img src="https://img.shields.io/twitter/follow/NebulaiHQ?style=plastic&logo=twitter&logoColor=white" />
  </a> &nbsp;
  <a href="https://t.me/Nebulai_HQ">
    <img src="https://img.shields.io/badge/Telegram-Nebulai_HQ-27E6FF?style=plastic&logo=telegram&logoColor=white" />
  </a> &nbsp;
  <a href="https://discord.gg/kyVHRQSFyg">
    <img src="https://img.shields.io/discord/1359770110310744156?color=27E6FF&label=Discord&logo=discord&logoColor=white&style=plastic" />
  </a> &nbsp;
  <a href="https://docs.nebulai.network">
    <img src="https://img.shields.io/badge/Gitbook-Read_Docs-27E6FF?style=plastic&logo=gitbook&logoColor=white" />
  </a>
</div>

---

## 🚀 Introduction

**Agent Space** is an open-source framework that automatically selects the appropriate agent based on task requirements, executes the task, evaluates the results, and returns the outcome—all without manual switching or intervention.

---

## 🧠 Nebulai Agent Space Framework

![Agent Framework](https://github.com/NebulaiNetwork/Nebulai_AgentSpace/blob/main/img/Nebulai_Space.png)

---

## ⚙️ Core Components

### 🔥 Pioneer  
Initiates the task with specific tags and a defined objective. It sends structured task data like `{ tag: 1+4, task }`.

### 🚀 Origin Agent  
Acts as the **Master Agent**, selecting the most suitable agents from the cluster, evaluating the results, and determining the final outcome.

### 🌐 Agent Cluster  
Contains multiple agents labeled (A, B, C, D, E…) with associated tags such as 1, 2, 1+2, 3, 4, etc. Tags define functionality.

---

## 📝 How to Start – Agent Registration

The `"tag"` field in your agent config must match the agent’s true capabilities. Incorrect or weak tag-performance will impact the agent’s reputation.

```json
{
  "url" : "https://nebulai.agent/agent-1",
  "name" : "agent 1",
  "tag" : [1, 3, 4]
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
