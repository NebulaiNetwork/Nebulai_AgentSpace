import psutil
from threading import Thread
from collections import deque

class AgentMonitor:
    def __init__(self, update_interval=5):
        self.agent_metrics = {}  # {agent_id: {'cpu': [], 'mem': [], 'tasks': 0}}
        self.update_interval = update_interval

    def start_monitoring(self, agent_id):
        self.agent_metrics[agent_id] = {
            'cpu': deque(maxlen=10),
            'mem': deque(maxlen=10),
            'tasks': 0
        }
        Thread(target=self._update_metrics, args=(agent_id,), daemon=True).start()

    def _update_metrics(self, agent_id):
        while True:
            proc = psutil.Process(os.getpid())  # 实际项目中需关联到具体智能体进程
            self.agent_metrics[agent_id]['cpu'].append(proc.cpu_percent())
            self.agent_metrics[agent_id]['mem'].append(proc.memory_percent())
            time.sleep(self.update_interval)

    def increment_tasks(self, agent_id):
        self.agent_metrics[agent_id]['tasks'] += 1

    def get_agent_load(self, agent_id):
        metrics = self.agent_metrics.get(agent_id, {})
        if not metrics:
            return 1.0  # 默认负载值
        # 综合计算负载指数 (CPU均值 + 内存均值 + 任务数*权重)
        avg_cpu = sum(metrics['cpu']) / len(metrics['cpu']) if metrics['cpu'] else 0
        avg_mem = sum(metrics['mem']) / len(metrics['mem']) if metrics['mem'] else 0
        return avg_cpu * 0.4 + avg_mem * 0.3 + metrics['tasks'] * 0.3