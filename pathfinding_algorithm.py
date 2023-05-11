class PathfindingAlgorithm:
    def __init__(self):
        pass

    @staticmethod
    def return_path(start_node, end_node):
        """
        Returns the path from the end node to the start node if a path is found (checked by the algorithm).
        :param start_node:  the start node
        :param end_node:    the end node, the goal
        :return: path:      a list of nodes ordered from the end node to the start node
        """
        current_node = start_node
        path = [current_node]
        while current_node.name != end_node.name:
            current_node = current_node.parent
            path.append(current_node)
        return path

    @staticmethod
    def expand_node(graph, current_node, closed_list, open_list):
        closed_list.append_node(current_node)  # the current node gets pushed to the closed list
        open_list.remove_node(current_node)
        if not current_node.adjacency_info:
            for adjacent_node in current_node.adjacency_info:
                open_list.append(graph.nodes[adjacent_node.name])


class AStar(PathfindingAlgorithm):
    pass


class BreathFirstSearch:
    pass


class SearchOrder:
    def __init__(self, search_type="queue"):
        self.search_type = search_type
        self.ordered_list = []

    def put(self, node):
        if self.search_type == "queue":
            self.ordered_list.append(node)
        elif self.search_type == "stack":
            self.ordered_list.append(node)

    def get(self, node):
        if self.search_type == "queue":
            return self.ordered_list.popleft()
        elif self.search_type == "stack":
            self.ordered_list.pop
