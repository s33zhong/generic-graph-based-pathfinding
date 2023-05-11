class Node:
    def __init__(self):
        self.name = None
        self.parent = []  # only written by pathfinding algorithm, should be a list of [node, path_number, edge_cost]
        self.f_cost = None  # This might be different for different algorithms, so only written by them as well


class WeightedMultiGraph:
    # We are not going to implement a uniform-cost multi-graph, as it is only a uniformly-weighted weighted multi-graph.
    # We also assume there is no self-loops of any kind, as it would not be very helpful for pathfinding.
    # Even though if once a node is on closed, it would not be expanded again, we just find it to be very contradictory
    #    as why bother looking for a path from a node to itself; it is not like we are getting anywhere. Then of course,
    #    it also induces a computation cost of O(n) at the worst case, as every node is always checked against itself.

    def __init__(self, graph_type):
        # The collection of nodes' names and its corresponding instances
        self.nodes = {}
        # The collection of nodes' names as keys, each with its adjacent nodes, edge index and cost as values
        self.adjacency_list = {}
        # The collection of nodes' adjacent nodes edges count; note the length of keys is equal to the length of keys
        #   of self.nodes
        self.adjacency_counts = {}
        self.graph_type = graph_type

    def generate_random_graph(self, size: int):
        pass

    def visualize_graph(self):
        pass

    def append_node(self, node: Node, adjacent_nodes: list, edge_costs: list):
        """
        Adds a new node with its adjacent nodes and the corresponding edge costs to the node list
        :param node:                a Node instance
        :param adjacent_nodes:      a list of Node instances of length n that node is connected to
        :param edge_costs:          a list of edge costs of length n that corresponding to the adjacent_nodes
        :return:
        """
        # add the new node to the graph
        if node is None:
            raise ValueError("A Node instance is required to call the append_node function.")
        else:
            self.nodes[node.name] = node

        adjacency_info = []
        if adjacent_nodes is not None and edge_costs is not None:
            for adjacent_node, edge_cost in adjacent_nodes, edge_costs:
                if adjacent_node.name == node.name:
                    raise ValueError("We assumed no self-looping nodes as it is not useful in pathfinding.")

                if adjacent_node.name in self.adjacency_counts.keys():  # At least one edge already exists
                    self.adjacency_counts[adjacent_node.name] += 1
                else:
                    self.adjacency_counts[adjacent_node.name] = 1

                edge_index = self.adjacency_counts[adjacent_node.name]

                if self.graph_type == "directed":
                    # record the adjacent nodes' info to be put into self.adjacency_list
                    adjacency_info.append([adjacent_node, edge_index, edge_cost])  # list of lists

                    # add this node back to the adjacent node entry; the edge index should be the same
                    self.adjacency_list[adjacent_node.name].append([node, edge_index,  edge_cost])

        self.adjacency_list[node.name] = adjacency_info  # add this nodes adjacency_info to the list

    def remove_node(self, node: Node):
        pass


class MultiGraph(WeightedMultiGraph):
    # Just a special case where it has uniform cost, so it is a subclass

    # we re-implement this method to ensure no edge cost is passed in
    def append_node(self, node: Node, adjacent_nodes: list, edge_costs):
        """
        Adds a new node with its adjacent nodes and the corresponding edge costs (all 1's) to the node list
        :param node:                a Node instance
        :param adjacent_nodes:      a list of Node instances of length n that node is connected to
        :param edge_costs:          a dummy parameter, just to be consistent with the parent class
        :return:
        """
        # add the new node to the graph
        if node is None:
            raise ValueError("A Node instance is required to call the append_node function.")
        else:
            self.nodes[node.name] = node

        adjacency_info = []
        if adjacent_nodes is not None and edge_costs is not None:
            for adjacent_node, edge_cost in adjacent_nodes, edge_costs:
                if adjacent_node.name in self.adjacency_counts.keys():
                    self.adjacency_counts[adjacent_node.name] += 1
                else:
                    self.adjacency_counts[adjacent_node.name] = 1

                edge_index = self.adjacency_counts[adjacent_node.name]
                if self.graph_type == "directed":
                    # record the adjacent nodes' info to be put into self.adjacency_list
                    adjacency_info.append([adjacent_node, edge_index, edge_cost])  # list of lists

                    # add this node back to the adjacent node entry; the edge index should be the same
                    self.adjacency_list[adjacent_node.name].append([node, edge_index,  edge_cost])

        self.adjacency_list[node.name] = adjacency_info  # add this nodes adjacency_info to the list

    def remove_node(self, node: Node):

        del self.nodes[node.name]

