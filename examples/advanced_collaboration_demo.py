"""
Advanced Collaboration Demo for SuperAI_Agents_Elysium
------------------------------------------------------
Demonstrates a coordinated workflow among multiple domains of AI agents,
featuring communication, task distribution, optimization, and monitoring.
"""

import time
from threading import Thread

from agents.collaborative_agent import CollaborativeAgent
from agents.task_agent import TaskAgent
from agents.communication_agent import CommunicationAgent
from agents.optimization_agent import OptimizationAgent
from agents.monitoring_agent import MemoryAgent

def simulate_task_execution(task_agent, task_description):
    print(f"{task_agent.name} is starting task: {task_description}")
    time.sleep(2)  # simulate work
    result = f"{task_agent.name} completed task: {task_description}"
    print(result)
    return result

def main():
    print("Starting Advanced Collaboration Demo...\n")

    # Instantiate agents
    coordinator = CollaborativeAgent("Coordinator")
    task_agent1 = TaskAgent("Data Analysis Agent")
    task_agent2 = TaskAgent("Reporting Agent")
    communication_agent = CommunicationAgent("Communication Agent")
    optimization_agent = OptimizationAgent("Optimization Agent")
    monitoring_agent = MemoryAgent()

    # Register task agents with coordinator
    coordinator.add_agent(task_agent1)
    coordinator.add_agent(task_agent2)

    # Set current tasks
    coordinator.current_tasks = [
        "Analyze financial market data",
        "Generate quarterly report"
    ]

    # Start optimization agent monitoring in background thread
    optimization_agent.monitor_and_optimize(coordinator)

    # Simulate task execution concurrently
    threads = []
    for task_agent, task_description in zip([task_agent1, task_agent2], coordinator.current_tasks):
        thread = Thread(target=simulate_task_execution, args=(task_agent, task_description))
        threads.append(thread)
        thread.start()

    # Wait for all tasks to complete
    for thread in threads:
        thread.join()

    # Collect results in coordinator (simulated)
    results = [f"Result from {agent.name}" for agent in coordinator.agents if hasattr(agent, 'name')]

    # Log results in monitoring agent
    for result in results:
        monitoring_agent.remember_short_term(result)

    print("\nMemoryAgent short-term memory contents:")
    print(monitoring_agent.recall_short_term())

    # Communication agent sends a summary message
    communication_agent.send_message("All tasks completed successfully.")

    # Stop optimization agent monitoring
    optimization_agent.stop()

    print("\nAdvanced Collaboration Demo completed.")

if __name__ == "__main__":
    main()
