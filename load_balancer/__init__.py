from .monitor import AgentMonitor
from .strategy import LoadStrategy, Strategy

class LoadBalancer:
    def __init__(self, strategy=Strategy.LEAST_LOADED):
        self.monitor = AgentMonitor()
        self.strategy = LoadStrategy(strategy)
        self.agents = {}  # {agent_id: {'weight': float, 'metadata': dict}}

    def register_agent(self, agent_id, weight=1.0, metadata=None):
        self.agents[agent_id] = {'weight': weight, 'metadata': metadata or {}}
        self.monitor.start_monitoring(agent_id)

    def dispatch_task(self, task_data):
        valid_agents = [a for a in self.agents if self._is_agent_healthy(a)]
        selected_agent = self.strategy.select_agent(valid_agents, self.monitor)
        self.monitor.increment_tasks(selected_agent)
        return selected_agent

    def _is_agent_healthy(self, agent_id):
        # 检查心跳或自定义健康指标
        return True