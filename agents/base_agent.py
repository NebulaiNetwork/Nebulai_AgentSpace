class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.message_queue = []
&nbsp;
&nbsp;

    def send_message(self, target_agent, message):
        target_agent.receive_message(self, message)
&nbsp;
&nbsp;

    def receive_message(self, sender, message):
        self.message_queue.append((sender.name, message))
        self.process_message(sender, message)
&nbsp;
&nbsp;

    def process_message(self, sender, message):
        raise NotImplementedError("This method should be overridden by subclasses.")
