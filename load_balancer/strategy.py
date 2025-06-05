from enum import Enum

class Strategy(Enum):
    ROUND_ROBIN = 1
    LEAST_LOADED = 2
    WEIGHTED_RANDOM = 3

class LoadStrategy:
    def __init__(self, strategy_type=Strategy.LEAST_LOADED):
        self.strategy = strategy_type
        self.last_agent = 0

    def select_agent(self, agent_ids, monitor):
        if self.strategy == Strategy.ROUND_ROBIN:
            self.last_agent = (self.last_agent + 1) % len(agent_ids)
            return agent_ids[self.last_agent]
        
        elif self.strategy == Strategy.LEAST_LOADED:
            return min(
                agent_ids, 
                key=lambda x: monitor.get_agent_load(x)
            )
        
        elif self.strategy == Strategy.WEIGHTED_RANDOM:
            loads = [1/monitor.get_agent_load(a) for a in agent_ids]
            return random.choices(agent_ids, weights=loads, k=1)[0]