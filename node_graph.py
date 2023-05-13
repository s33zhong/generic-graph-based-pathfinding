import networkx as nx
import numpy as np

class Node:
    def __init__(self, name: str):
        self.name = name
        self.adjacency_info = []  # only written when constructing the graph with __init__ method of WeightedMultigraph
        self.parent = []  # only written by pathfinding algorithm; a list of [parent_node, edge_index, edge_cost]

        # These might be different for different algorithms, so only written by them as well
        self.f_cost = None
        self.g_cost = None
        self.h_cost = None
        self.optimal_cost = None

        # Need this for calculating the heuristic cost
        self.x = None
        self.y = None


class WeightedGraph:
    def __init__(self, graph_type="undirected"):
        # The collection of nodes' names and its corresponding instances
        self.nodes = {}
        self.graph_type = graph_type

    def generate_random_graph(self, size: int):
        pass

    def generate_square_grid(self, width: int, height: int):
        for i in range(height):
            for j in range(width):
                generated_node = Node(name="node {}".format(i * j))

                # need this for calculating the heuristic cost
                generated_node.x = i
                generated_node.y = j
                adjacency_info = []
                if i != 0:  # if not the first row
                    adjacency_info.append({'node name': "node {}".format(i * (j - 1)), 'edge cost': 1})
                if i != height - 1:  # if not the last row
                    adjacency_info.append({'node name': "node {}".format(i * (j + 1)), 'edge cost': 1})
                if j != 0:  # if not the first column
                    adjacency_info.append({'node name': "node {}".format(i * j - 1), 'edge cost': 1})
                if j != width - 1:  # if not the last column
                    adjacency_info.append({'node name': "node {}".format(i * j + 1), 'edge cost': 1})

                generated_node.adjacency_info = adjacency_info  # add this node's adjacency_info to it
                self.nodes[generated_node.name] = generated_node  # add this node to the graph
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
        if adjacent_nodes is not None and edge_costs is not None:
            for adjacent_node, edge_cost in zip(adjacent_nodes, edge_costs):
                node_edge_count += 1
                # print("The adjacent node is: {}\n".format(adjacent_node.name),
                #       "The edge cost is: {}\n".format(edge_cost))
                if adjacent_node.name == current_node.name:
                    raise ValueError("We assumed no self-looping nodes as it is not useful in pathfinding.")

                if self.graph_type == "undirected":  # add the edge back if is an undirected graph
                    # record the adjacent nodes' info to be put into node.adjacency_info
                    #   note the node instance can be accessed through self.nodes[node.name]
                    adjacency_info.append({"node name": adjacent_node.name,
                                           "edge cost": edge_cost})

                    # add this node back to the adjacent node's attribute; the edge index should be the same
                    self.nodes[adjacent_node.name].adjacency_info.append({"node name": current_node.name,
                                                                          "edge cost": edge_cost})

        current_node.adjacency_info = adjacency_info  # add this nodes adjacency_info to the node
        self.edge_counts[current_node.name] = node_edge_count
        self.nodes[current_node.name] = current_node

    def remove_node(self, node: Node):
        pass


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

    def generate_square_grid(self, width: int, height: int):
        for i in range(height):
            for j in range(width):
                current_node_count = i * width + j
                generated_node = Node(name="node {}".format(current_node_count))

                # need this for calculating the heuristic cost
                generated_node.x = i
                generated_node.y = j
                adjacency_info = []

                if i != 0:  # if not the first row
                    adjacency_info.append({'node name': "node {}".format(current_node_count - width),
                                           'edge cost': 1})  # the node above
                if i != height - 1:  # if not the last row
                    adjacency_info.append({'node name': "node {}".format(current_node_count + width),
                                           'edge cost': 1})  # the node below
                if j != 0:  # if not the first column
                    adjacency_info.append({'node name': "node {}".format(current_node_count - 1),
                                           'edge cost': 1})  # the node to the left
                if j != width - 1:  # if not the last column
                    adjacency_info.append({'node name': "node {}".format(current_node_count + 1),
                                           'edge cost': 1})  # the node to the right

                generated_node.adjacency_info = adjacency_info  # add this node's adjacency_info to it
                self.nodes[generated_node.name] = generated_node  # add this node to the graph

    def visualize_graph(self):
        nx_graph = nx.Graph()

        for node in self.nodes.values():
            nx_graph.add_node(node.name)
            for adjacent_node in node.adjacency_info:
                nx_graph.add_edge(node.name, adjacent_node['node name'],
                                  weight=adjacent_node['edge cost'])

        nx.draw_networkx(nx_graph, with_labels=True, font_weight='bold')

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
                # print("The adjacent node is: {}\n".format(adjacent_node.name),
                #       "The edge cost is: {}\n".format(edge_cost))
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
                    adjacency_info.append({"node name": adjacent_node.name,
                                           "edge index": edge_index,
                                           "edge cost": edge_cost})

                    # add this node back to the adjacent node's attribute; the edge index should be the same
                    self.nodes[adjacent_node.name].adjacency_info.append({"node name": current_node.name,
                                                                          "edge index": edge_index,
                                                                          "edge cost": edge_cost})

        current_node.adjacency_info = adjacency_info  # add this nodes adjacency_info to the node
        self.edge_counts[current_node.name] = node_edge_count
        self.nodes[current_node.name] = current_node

    def remove_node(self, node: Node):
        pass



#%%
