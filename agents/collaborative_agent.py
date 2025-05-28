from .base_agent import BaseAgent
&nbsp;
&nbsp;

class CollaborativeAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name)
        self.agents = []
&nbsp;
&nbsp;

    def add_agent(self, agent):
        self.agents.append(agent)
&nbsp;
&nbsp;

    def coordinate_tasks(self, task):
        for agent in self.agents:
            agent.send_message(self, task)
&nbsp;
&nbsp;

    def process_message(self, sender, message):
        print(f"{self.name} received a message from {sender.name}: {message}")
        # Handle the message and coordinate responses
