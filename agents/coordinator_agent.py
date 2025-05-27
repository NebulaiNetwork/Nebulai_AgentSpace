"""
CoordinatorAgent
-----------------
Coordinates workflow and communication between multiple agents for collaborative problem-solving.
"""
&nbsp;
&nbsp;

from agents.genius_ai import GeniusAI
&nbsp;
&nbsp;

class CoordinatorAgent:
    def __init__(self):
        self.genius_ai = GeniusAI()
&nbsp;
&nbsp;

    def run_collaboration(self, problem: str) -> str:
        """
        Coordinate agents workflow for solving a problem.
        """
        print(f"Coordinator: Starting problem solving for: {problem}")
&nbsp;
&nbsp;

        # GeniusAI orchestrates understanding, creativity, and validation
        solution = self.genius_ai.solve(problem)
&nbsp;
&nbsp;

        print("Coordinator: Collaboration complete.")
        return solution
