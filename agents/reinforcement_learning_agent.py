"""
ReinforcementLearningAgent
--------------------------
Implements a reinforcement learning agent with Q-learning for dynamic decision making.
"""
&nbsp;
&nbsp;

import numpy as np
&nbsp;
&nbsp;

class ReinforcementLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, gamma=0.95):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))
        self.learning_rate = learning_rate
        self.gamma = gamma
&nbsp;
&nbsp;

    def choose_action(self, state, epsilon):
        import random
        if random.uniform(0,1)  epsilon:
            return random.randint(0, self.action_size -1)  # explore
        else:
            return np.argmax(self.q_table[state])  # exploit
&nbsp;
&nbsp;

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state][action]
        target = reward + self.gamma * np.max(self.q_table[next_state])
        self.q_table[state][action] += self.learning_rate * (target - predict)
