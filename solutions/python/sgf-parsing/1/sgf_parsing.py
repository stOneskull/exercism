from dataclasses import dataclass, field


@dataclass
class SgfTree:
    properties: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


def parse(go):
    tree, _ = parse_tree(go)
    return tree


def parse_tree(go, i=0):
    if i >= len(go) or go[i] != '(':
        raise ValueError("tree missing")

    i += 1
    tree, i = parse_sequence(go, i)
    i += 1 
    return tree, i


def parse_sequence(go, i):
    nodes = []

    while go[i] == ';':
        i += 1
        prop_key_start = i

        while go[i].isalpha():
            if not go[i].isupper():
                raise ValueError("property must be in uppercase")
            i += 1

        i = prop_key_start

        properties, i = parse_properties(go, i)
        
        children = []

        while go[i] == '(':
            child_tree, i = parse_tree(go, i)
            children.append(child_tree)
        
        nodes.append(SgfTree(properties, children))

    if not nodes:
        raise ValueError("tree with no nodes")
    
    for j in range(len(nodes) - 1):
        nodes[j].children.append(nodes[j+1])

    return nodes[0], i


def parse_properties(go, i):
    props = {}
    
    while go[i] not in (';()'):
        key_start = i
        while go[i].isupper():
            i += 1
        key = go[key_start:i]

        if go[i] != '[':
            raise ValueError("properties without delimiter")

        values = []

        while go[i] == '[':
            i += 1
            val_start = i
            while go[i] != ']':
                if go[i] == '\\':
                    i += 1
                i += 1

            raw_value = go[val_start:i]
            value = parse_value(raw_value)
            values.append(value)
            i += 1
        
        props[key] = values

    return props, i


def parse_value(raw_value):
    value = ""

    k = 0
    while k < len(raw_value):
        if raw_value[k] == '\\':
            k += 1
            if k < len(raw_value):
                if raw_value[k] == '\n':
                    pass
                elif raw_value[k] == '\t':
                    value += ' '
                else:
                    value += raw_value[k]
        elif raw_value[k] == '\t':
            value += ' '
        else:
            value += raw_value[k]
        k += 1

    return value
    