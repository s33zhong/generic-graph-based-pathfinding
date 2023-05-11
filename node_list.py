class NodeList:
    def __init__(self):
        self.nodes = {}

    def append_node(self, node):
        if node.name in self.nodes.keys():
            print("Append failed. Node {} is already in this NodeList instance.".format(node.name))
        else:
            self.nodes[node.name] = node


class ClosedList(NodeList):
    pass


class OpenList(NodeList):
    def remove_node(self, node):
        if node.name not in self.nodes.keys() or not self.nodes.keys():  # node does not exist or empty open list
            print("Remove failed. Node {} is not in the open list.".format(node.name))
        else:
            self.nodes[node.name] = node
