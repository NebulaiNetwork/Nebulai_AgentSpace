from .base_agent import BaseAgent
&nbsp;
&nbsp;

class TaskAgent(BaseAgent):
    def process_message(self, sender, message):
        print(f"{self.name} is processing task: {message}")
        # Simulate task processing
        result = f"Result of {message} by {self.name}"
        self.send_message(sender, result)
