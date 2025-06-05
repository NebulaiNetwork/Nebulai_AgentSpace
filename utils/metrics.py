import psutil
import time
from typing import Dict, Deque, Optional
from collections import deque

class ResourceMetrics:
    """
    采集和管理智能体的资源指标数据，包括：
    - CPU 使用率（滑动窗口平均值）
    - 内存占用率
    - 任务队列长度
    - 网络 I/O（可选）
    """
    
    def __init__(self, window_size: int = 10):
        """
        :param window_size: 滑动窗口大小（用于平滑指标波动）
        """
        self.window_size = window_size
        self.cpu_history: Deque[float] = deque(maxlen=window_size)
        self.mem_history: Deque[float] = deque(maxlen=window_size)
        self.task_count: int = 0
        self.last_network_io = None
        self.last_update_time = time.time()

    def update(self) -> None:
        """更新所有指标"""
        # CPU 使用率（百分比）
        self.cpu_history.append(psutil.cpu_percent(interval=0.1))
        
        # 内存占用率（当前进程）
        process = psutil.Process()
        self.mem_history.append(process.memory_percent())
        
        # 网络 I/O（可选，适用于分布式场景）
        net_io = psutil.net_io_counters()
        if self.last_network_io:
            delta = net_io.bytes_sent - self.last_network_io.bytes_sent
            # 可在此计算网络吞吐量指标
        self.last_network_io = net_io
        
        self.last_update_time = time.time()

    def get_cpu_load(self, use_window_avg: bool = True) -> float:
        """返回 CPU 负载（当前值或滑动窗口平均值）"""
        return sum(self.cpu_history) / len(self.cpu_history) if use_window_avg else self.cpu_history[-1]

    def get_mem_load(self) -> float:
        """返回内存占用率（最新值）"""
        return self.mem_history[-1] if self.mem_history else 0.0

    def increment_tasks(self, count: int = 1) -> None:
        """增加待处理任务计数"""
        self.task_count += count

    def get_combined_load(self, weights: Optional[Dict[str, float]] = None) -> float:
        """
        计算综合负载指数（加权平均值）
        
        :param weights: 各指标的权重，例如:
            {"cpu": 0.4, "memory": 0.3, "tasks": 0.3}
            默认权重为均分
        """
        weights = weights or {"cpu": 0.4, "memory": 0.3, "tasks": 0.3}
        return (
            self.get_cpu_load() * weights["cpu"]
            + self.get_mem_load() * weights["memory"]
            + self.task_count * weights["tasks"]
        )

    def reset(self) -> None:
        """重置所有指标（用于智能体重启时）"""
        self.cpu_history.clear()
        self.mem_history.clear()
        self.task_count = 0