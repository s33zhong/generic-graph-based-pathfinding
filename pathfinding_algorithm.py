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

    def expand_node(self, current_node, closed_list, open_list):
        closed_list.append(current_node)  # the current node gets pushed to the closed list



class AStar(PathfindingAlgorithm):
    pass

#%%
