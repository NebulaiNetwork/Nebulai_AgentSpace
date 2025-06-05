def test_least_loaded_strategy():
    balancer = LoadBalancer()
    balancer.register_agent("agent1", weight=1.0)
    balancer.register_agent("agent2", weight=2.0)
    
    # 模拟agent1高负载
    balancer.monitor.agent_metrics["agent1"]['cpu'].extend([80, 85, 90])
    
    selected = balancer.dispatch_task({})
    assert selected == "agent2"