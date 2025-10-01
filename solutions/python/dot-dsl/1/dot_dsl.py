from dataclasses import dataclass



NODE, EDGE, ATTR = range(3)


@dataclass
class Node:
    name: str
    attrs: dict


@dataclass
class Edge:
    src: str
    dst: str
    attrs: dict



class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is None:
            return

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for item in data:
            if not isinstance(item, tuple) or len(item) < 3:
                raise TypeError("Graph item incomplete")

            match item[0]:
                case 0:
                    if len(item) != 3:
                        raise ValueError("Node is malformed")
                    self.add_node(*item[1:])
                case 1:
                    if len(item) != 4:
                        raise ValueError("Edge is malformed")
                    self.add_edge(*item[1:])
                case 2:
                    if len(item) != 3:
                        raise ValueError("Attribute is malformed")
                    self.add_attr(*item[1:])
                case _:
                    raise ValueError("Unknown item")

    def add_node(self, name, attrs):
        self.nodes.append(Node(name, attrs))

    def add_edge(self, src, dst, attrs):
        self.edges.append(Edge(src, dst, attrs))

    def add_attr(self, name, value):
        self.attrs[name] = value
