class Agent:
    def __init__(self, id, weight=1.0):
        self.id = id
        self.weight = weight  # 用于加权负载策略
        
    @property
    def current_load(self):
        """可被重写以提供自定义负载指标"""
        return 0