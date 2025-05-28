"""
MetaLearningAgent
-----------------
Enhances learning efficiency by learning how to learn from multiple tasks and adapt quickly.
"""
&nbsp;
&nbsp;

class MetaLearningAgent:
    def __init__(self):
        self.task_experience = {}
&nbsp;
&nbsp;

    def learn_task(self, task_name: str, performance_score: float):
        self.task_experience[task_name] = performance_score
        print(f"MetaLearningAgent: Learned task '{task_name}' with score {performance_score:.2f}")
&nbsp;
&nbsp;

    def adapt_to_new_task(self, new_task_name: str):
        best_task = max(self.task_experience, key=self.task_experience.get, default=None)
        if best_task:
            print(f"MetaLearningAgent: Adapting knowledge from best task '{best_task}' to new task '{new_task_name}'")
        else:
            print(f"MetaLearningAgent: No prior tasks; learning new task '{new_task_name}' from scratch")
