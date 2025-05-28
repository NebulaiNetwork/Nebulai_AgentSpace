"""
MemoryAgent
------------
Manages shared memory stores for context persistence across agents.
"""
&nbsp;
&nbsp;

import datetime
&nbsp;
&nbsp;

class MemoryAgent:
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = []
&nbsp;
&nbsp;

    def remember_short_term(self, info: str):
        timestamp = datetime.datetime.now().isoformat()
        self.short_term_memory.append((timestamp, info))
        print(f"MemoryAgent: Short-term memory updated at {timestamp}.")
&nbsp;
&nbsp;

    def remember_long_term(self, info: str):
        timestamp = datetime.datetime.now().isoformat()
        self.long_term_memory.append((timestamp, info))
        print(f"MemoryAgent: Long-term memory updated at {timestamp}.")
&nbsp;
&nbsp;

    def recall_short_term(self):
        return self.short_term_memory[-5:]
&nbsp;
&nbsp;

    def recall_long_term(self):
        return self.long_term_memory[-10:]
