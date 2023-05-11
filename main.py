import node_graph, node_list, pathfinding_algorithm

if __name__ == "__main__":
    graph = node_graph.WeightedMultiGraph()
    node_1 = node_graph.Node(name='node 1')
    node_1p = node_graph.Node(name='node 1 prime')
    node_2 = node_graph.Node(name='node 2')

    graph.append_node(node_1)
    graph.append_node(node_1p)
    graph.append_node(node_2, adjacent_nodes=[node_1, node_1p, node_1, node_1p], edge_costs=[1, 2, 2, 2])
    graph


#%%
