class Node:
    def __init__(self, name: str):
        self.name = name
        self.adjacency_info = []  # only written when constructing the graph with __init__ method of WeightedMultigraph
        self.parent = []  # only written by pathfinding algorithm, should be a list of [node, path_number, edge_cost]
        self.f_cost = None  # This might be different for different algorithms, so only written by them as well


class WeightedMultiGraph:
    # We are not going to implement a uniform-cost multi-graph, as it is only a uniformly-weighted weighted multi-graph.
    # We also assume there is no self-loops of any kind, as it would not be very helpful for pathfinding.
    # Even though if once a node is on closed, it would not be expanded again, we just find it to be very contradictory
    #    as why bother looking for a path from a node to itself; it is not like we are getting anywhere. Then of course,
    #    it also induces a computation cost of O(n) at the worst case, as every node is always checked against itself.

    def __init__(self, graph_type="directed"):
        # The collection of nodes' names and its corresponding instances
        self.nodes = {}
        # The collection of nodes' adjacent nodes edges count; note the length of keys is equal to the length of keys
        #   of self.nodes
        self.edge_counts = {}
        self.adjacent_node_count = {}
        self.graph_type = graph_type

    def generate_random_graph(self, size: int):
        pass

    def visualize_graph(self):
        pass

    def append_node(self, current_node: Node, adjacent_nodes=None, edge_costs=None):
        """
        Adds a new node with its adjacent nodes and the corresponding edge costs to the node list
        :param current_node:                a Node instance
        :param adjacent_nodes:      a list of Node instances of length n that node is connected to
        :param edge_costs:          a list of edge costs of length n that corresponding to the adjacent_nodes
        :return:
        """
        # add the new node to the graph
        if current_node is None:
            raise ValueError("A Node instance is required to call the append_node function.")

        adjacency_info = []
        node_edge_count = 0
        node_adjacent_node_count = 0
        if adjacent_nodes is not None and edge_costs is not None:
            for adjacent_node, edge_cost in zip(adjacent_nodes, edge_costs):
                node_edge_count += 1
                print("The adjacent node is: {}\n".format(adjacent_node.name),
                      "The edge cost is: {}\n".format(edge_cost))
                if adjacent_node.name == current_node.name:
                    raise ValueError("We assumed no self-looping nodes as it is not useful in pathfinding.")

                if adjacent_node.name in self.edge_counts.keys():  # At least one edge already exists
                    self.edge_counts[adjacent_node.name] += 1
                else:
                    self.edge_counts[adjacent_node.name] = 1
                    self.adjacent_node_count[adjacent_node.name] += 1

                edge_index = self.edge_counts[adjacent_node.name]

                if self.graph_type == "directed":  # add the edge back if is a directed graph
                    # record the adjacent nodes' info to be put into node.adjacency_info
                    #   note the node instance can be accessed through self.nodes[node.name]
                    adjacency_info.append({"adjacent node name": adjacent_node.name,
                                           "edge index": edge_index,
                                           "edge cost": edge_cost})

                    # add this node back to the adjacent node's attribute; the edge index should be the same
                    self.nodes[adjacent_node.name].adjacency_info.append({"adjacent node name": current_node.name,
                                                                          "edge index": edge_index,
                                                                          "edge cost": edge_cost})

        current_node.adjacency_info = adjacency_info  # add this nodes adjacency_info to the node
        self.edge_counts[current_node.name] = node_edge_count
        self.nodes[current_node.name] = current_node

    def remove_node(self, node: Node):
        pass


class MultiGraph(WeightedMultiGraph):
    # Just a special case where it has uniform cost, so it is a subclass

    pass
