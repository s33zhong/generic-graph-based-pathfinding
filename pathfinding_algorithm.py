import collections
import heapq


# We only store node names in the node lists, to save memory, as accessing Node.nodes dict (hash table) is only O(1)
class ClosedList:
    def __init__(self):
        self.node_names = set()

    def add_node(self, node_name):
        self.node_names.add(node_name)

    def exist(self, node_name):
        return node_name in self.node_names


class OpenList:
    def __init__(self, list_type="queue"):
        self.record = []
        if list_type in {"queue", "stack"}:
            # need order, so deque. O(1) to append and pop,
            # implements queue & stack
            self.node_names = collections.deque()
        elif list_type in {"priority_queue"}:
            self.node_names = []
        self.list_type = list_type

    def pop_node(self):
        result = None
        if self.node_names:
            if self.list_type == "queue":
                result = self.node_names.popleft()
            elif self.list_type == "stack":
                result = self.node_names.pop()
            elif self.list_type == "priority_queue":
                result = heapq.heappop(self.node_names)[1]
        return result

    def add_node(self, closed_list, node_name, priority=0):
        if closed_list.exist(node_name):  # node already exists
            return False
        else:
            if self.list_type == "priority_queue":
                heapq.heappush(self.node_names, (priority, node_name))
            elif self.list_type in {"queue", "stack"}:
                self.node_names.append(node_name)  # attach to the right
                self.record.append(node_name)
            return True

    def empty(self):
        return not self.node_names


class PathfindingAlgorithm:
    def __init__(self):
        self.current_node = None

    @staticmethod
    def return_path(start_node, end_node, order):
        """
        Returns the path from the end node to the start node if a path is found (checked by the algorithm).
        :param order:       whether the returned path should be from the end node or from the start node
        :param start_node:  the start node
        :param end_node:    the end node, the goal
        :return: path:      a list of nodes ordered from the end node to the start node
        """
        current_node = end_node
        path = []
        # print(current_node.name)
        while current_node.name != start_node.name:
            # if not current_node.parent:  # no parent node, must be the start node
            #     break
            path.append(current_node.name)
            current_node = current_node.parent
        path.append(start_node.name)  # add the name back for consistency
        if order == 'reversed':  # from the end
            return path
        elif order == 'forward':  # from the start
            path.reverse()
            return path


class BreathFirstSearch(PathfindingAlgorithm):

    def find_path(self, graph, start_node, end_node, order='reversed'):
        """
        Implements a BFS algorithm that does not care about optimal cost (just for practice purposes)
        :param graph:           a WeightedMultigraph instance
        :param start_node:      a Node instance, where we are starting
        :param end_node:        a Node instance, our goal
        :param order:           the path with node names, takes on either 'forward' or 'reversed'
        :return:
        """
        open_list = OpenList(list_type="queue")  # BreathFirstSearch implements a queue
        closed_list = ClosedList()
        open_list.add_node(closed_list=closed_list, node_name=start_node.name)
        current_node = None
        while not open_list.empty():
            current_node = graph.nodes[open_list.pop_node()]  # get the current node!
            # print("Current node is: {} & the end node is: {}".format(current_node.name,
            #                                                          end_node.name))
            if current_node.name == end_node.name:
                print(open_list.record)
                return self.return_path(start_node=start_node, end_node=end_node, order=order)

            if not closed_list.exist(current_node.name):  # this node does not currently exist in the closed list
                closed_list.add_node(current_node.name)
                for adjacent_node_info in current_node.adjacency_info:
                    adjacent_node_name = adjacent_node_info['node name']
                    adjacent_node = graph.nodes[adjacent_node_name]
                    added_to_queue = open_list.add_node(closed_list=closed_list, node_name=adjacent_node.name)
                    if added_to_queue:
                        adjacent_node.parent = current_node


class DijkstraSearch(PathfindingAlgorithm):
    def find_path(self, graph, start_node, end_node, order='reversed'):
        open_list = OpenList(list_type="priority_queue")  # BreathFirstSearch implements a queue
        closed_list = ClosedList()
        open_list.add_node(closed_list=closed_list, node_name=start_node.name)
        # while not open_list.empty():


