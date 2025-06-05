from fastapi import APIRouter
from . import LoadBalancer

router = APIRouter()
balancer = LoadBalancer()

@router.get("/agents/load")
async def get_load_status():
    return {
        agent: {
            "load": balancer.monitor.get_agent_load(agent),
            "weight": balancer.agents[agent]['weight']
        }
        for agent in balancer.agents
    }