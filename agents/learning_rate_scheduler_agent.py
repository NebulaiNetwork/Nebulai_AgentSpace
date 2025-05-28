"""
LearningRateSchedulerAgent
--------------------------
Dynamically adjusts learning rates of ML models during training for optimized convergence.
"""
&nbsp;
&nbsp;

class LearningRateSchedulerAgent:
    def __init__(self, initial_lr=0.01, decay_rate=0.1):
        self.lr = initial_lr
        self.decay_rate = decay_rate
        self.epoch = 0
&nbsp;
&nbsp;

    def step(self):
        self.epoch += 1
        self.lr = self.lr * (1 / (1 + self.decay_rate * self.epoch))
        print(f"Epoch {self.epoch}: Adjusted learning rate to {self.lr:.6f}")
        return self.lr
