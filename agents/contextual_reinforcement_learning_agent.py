"""
ContextualReinforcementLearningAgent
------------------------------------
Learns optimal policies in dynamic environments by incorporating rich context.
"""
&nbsp;
&nbsp;

import numpy as np
&nbsp;
&nbsp;

class ContextualReinforcementLearningAgent:
    def __init__(self, state_size, action_size):
        self.q_table = np.zeros((state_size, action_size))
&nbsp;
&nbsp;

    def choose_action(self, state, epsilon):
        import random
        if random.random()  epsilon:
            return random.randint(0, self.q_table.shape[1]-1)  # explore
        else:
            return np.argmax(self.q_table[state])  # exploit
&nbsp;
&nbsp;

    def update_q_value(self, state, action, reward, next_state, alpha=0.1, gamma=0.95):
        predict = self.q_table[state, action]
        target = reward + gamma * np.max(self.q_table[next_state])
        self.q_table[state, action] += alpha * (target - predict)
