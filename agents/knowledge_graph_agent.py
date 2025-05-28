"""
KnowledgeGraphAgent
-------------------
Manages knowledge representation, reasoning over graph structures,
and semantic relationship extraction for enhanced understanding.
"""
&nbsp;
&nbsp;

import networkx as nx
&nbsp;
&nbsp;

class KnowledgeGraphAgent:
    def __init__(self):
        self.graph = nx.Graph()
&nbsp;
&nbsp;

    def add_entity(self, entity: str):
        self.graph.add_node(entity)
&nbsp;
&nbsp;

    def add_relation(self, entity1: str, entity2: str, relation: str):
        self.graph.add_edge(entity1, entity2, relation=relation)
&nbsp;
&nbsp;

    def query_relation(self, entity1: str, entity2: str):
        if self.graph.has_edge(entity1, entity2):
            return self.graph.edges[entity1, entity2]['relation']
        else:
            return f"No direct relation between {entity1} and {entity2}."
&nbsp;
&nbsp;

    def find_related_entities(self, entity: str):
        if entity not in self.graph:
            return []
        neighbors = list(self.graph.neighbors(entity))
        return neighbors
