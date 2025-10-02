from json import dumps
from itertools import takewhile
from copy import deepcopy


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __str__(self, indent=None):
        return dumps(self.to_dict(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def to_dict(self):
        return {self.label: [c.to_dict() for c in sorted(self.children)]}
    
    def from_pov(self, from_node):
        new_tree = deepcopy(self)
        path_to_new_root = new_tree.path_from_root(from_node)
        if not path_to_new_root or path_to_new_root[-1].label != from_node:
            raise ValueError("Tree could not be reoriented")

        for i in range(len(path_to_new_root)-1, 0, -1):
            parent, child = path_to_new_root[i-1], path_to_new_root[i]
            parent.children.remove(child)
            child.children.append(parent)

        return path_to_new_root[-1]

    def path_to(self, from_node, to_node):
        path_from = self.path_from_root(from_node)
        path_to = self.path_from_root(to_node)

        if not path_from or path_from[-1].label != from_node:
            raise ValueError("Tree could not be reoriented")
        if not path_to or path_to[-1].label != to_node:
            raise ValueError("No path found")

        # Find lowest common ancestor
        common_path = list(takewhile(lambda x: x[0] == x[1], zip(path_from, path_to)))
        lca_index = len(common_path) - 1

        # Path from 'from_node' up to LCA, then down to 'to_node'
        up_path = [node.label for node in path_from[lca_index:]]
        down_path = [node.label for node in path_to[lca_index+1:]]

        return up_path[::-1] + down_path

    def path_from_root(self, to_node_label, path=None):
        path = path or [self]
        if self.label == to_node_label:
            return path
        for child in self.children:
            found_path = child.path_from_root(to_node_label, path + [child])
            if found_path:
                return found_path
