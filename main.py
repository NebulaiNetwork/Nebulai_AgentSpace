from agents.collaborative_agent import CollaborativeAgent
from agents.task_agent import TaskAgent
from agents.communication_agent import CommunicationAgent
&nbsp;
&nbsp;

def main():
    # Create agents
    coordinator = CollaborativeAgent("Coordinator")
    task_agent1 = TaskAgent("Task Agent 1")
    task_agent2 = TaskAgent("Task Agent 2")
    comm_agent = CommunicationAgent("Communication Agent")
&nbsp;
&nbsp;

    # Set up collaboration
    coordinator.add_agent(task_agent1)
    coordinator.add_agent(task_agent2)
&nbsp;
&nbsp;

    # Start task coordination
    coordinator.coordinate_tasks("Analyze data for project X")
&nbsp;
&nbsp;

if __name__ == "__main__":
    main()
