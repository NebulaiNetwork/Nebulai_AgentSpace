"""
Basic Usage Demo for SuperAI_Agents_Elysium
-------------------------------------------
Demonstrates simple initialization and interaction with selected high-tech agents.
"""

from agents.genius_ai import GeniusAI
from agents.dialogue_agent import DialogueAgent
from agents.creativity_agent import CreativityAgent

def main():
    print("Starting Basic Usage Demo...\n")

    # Initialize GeniusAI agent
    genius_ai = GeniusAI()
    problem = "Optimize traffic flow in urban area"
    solution = genius_ai.solve(problem)
    print(f"GeniusAI solution for problem '{problem}':\n{solution}\n")

    # Simple dialogue interaction
    dialogue = DialogueAgent()
    user_input = "What is the weather like today?"
    response = dialogue.respond(user_input)
    print(f"DialogueAgent response to '{user_input}':\n{response}\n")

    # Creativity agent idea generation
    creativity = CreativityAgent()
    creative_prompt = "Innovative uses of solar energy"
    ideas = creativity.create_ideas(creative_prompt)
    print(f"CreativityAgent ideas for '{creative_prompt}':\n{ideas}\n")

    print("Basic Usage Demo completed.")

if __name__ == "__main__":
    main()

