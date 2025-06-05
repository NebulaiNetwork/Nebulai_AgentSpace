from load_balancer import LoadBalancer

class AgentSpace:
    def __init__(self):
        self.balancer = LoadBalancer()
        
    def add_agent(self, agent, weight=1.0):
        self.balancer.register_agent(agent.id, weight)
        # ...原有注册逻辑

    def dispatch(self, task):
        agent_id = self.balancer.dispatch_task(task)
        return self._send_to_agent(agent_id, task)