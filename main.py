"""
Super Advanced Multi-Agent System
----------------------------------
This script demonstrates a powerful and feature-rich multi-agent system
with collaborative task management and communication capabilities.
"""

from agents.collaborative_agent import CollaborativeAgent
from agents.task_agent import TaskAgent
from agents.communication_agent import CommunicationAgent
from agents.logging_agent import LoggingAgent
from agents.analytics_agent import AnalyticsAgent
from agents.monitoring_agent import MonitoringAgent

def main():
    # Create agents
    coordinator = CollaborativeAgent("Coordinator")
    task_agent1 = TaskAgent("Task Agent 1")
    task_agent2 = TaskAgent("Task Agent 2")
    comm_agent = CommunicationAgent("Communication Agent")
    logging_agent = LoggingAgent("Logging Agent")
    analytics_agent = AnalyticsAgent("Analytics Agent")
    monitoring_agent = MonitoringAgent("Monitoring Agent")

    # Set up collaboration
    coordinator.add_agent(task_agent1)
    coordinator.add_agent(task_agent2)
    coordinator.add_agent(comm_agent)
    coordinator.add_agent(logging_agent)
    coordinator.add_agent(analytics_agent)
    coordinator.add_agent(monitoring_agent)

    # Start task coordination
    task_description = "Analyze data for project X"
    logging_agent.log(f"Starting task coordination for: {task_description}")
    coordinator.coordinate_tasks(task_description)

    # Monitor progress
    monitoring_agent.monitor_agents(coordinator.agents)
    
    # Communicate results
    results = coordinator.collect_results()
    comm_agent.send_message("Project X Analysis Results", results)

    # Perform analytics on the results
    analytics_report = analytics_agent.analyze(results)
    logging_agent.log(f"Analytics Report: {analytics_report}")

if __name__ == "__main__":
    main()
