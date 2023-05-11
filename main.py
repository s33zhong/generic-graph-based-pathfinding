import node_graph, node_list, pathfinding_algorithm

if __name__ == "__main__":
    graph = node_graph.WeightedMultiGraph()
    node_1 = node_graph.Node(name='node 1')
    node_2 = node_graph.Node(name='node 2')
    node_3 = node_graph.Node(name='node 3')
    node_4 = node_graph.Node(name='node 4')
    node_5 = node_graph.Node(name='node 5')
    node_6 = node_graph.Node(name='node 6')
    node_7 = node_graph.Node(name='node 7')

    graph.append_node(node_1)
    graph.append_node(node_2, adjacent_nodes=[node_1], edge_costs=[1])
    graph.append_node(node_3, adjacent_nodes=[node_1], edge_costs=[1])
    graph.append_node(node_4, adjacent_nodes=[node_3], edge_costs=[6])
    graph.append_node(node_5, adjacent_nodes=[node_4], edge_costs=[4])
    graph.append_node(node_6, adjacent_nodes=[node_3], edge_costs=[2])
    graph.append_node(node_7, adjacent_nodes=[node_2], edge_costs=[2])

    bfs_alg = pathfinding_algorithm.BreathFirstSearch()
    print(bfs_alg.find_path(graph, node_1, node_7, "forward"))

    dfs_alg = pathfinding_algorithm.BreathFirstSearch()
    print(dfs_alg.find_path(graph, node_1, node_7, "forward"))


#%%
