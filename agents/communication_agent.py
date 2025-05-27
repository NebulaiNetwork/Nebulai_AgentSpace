from .base_agent import BaseAgent
&nbsp;
&nbsp;

class CommunicationAgent(BaseAgent):
    def process_message(self, sender, message):
        print(f"{self.name} received a message: {message}")
        # Handle communication logic
