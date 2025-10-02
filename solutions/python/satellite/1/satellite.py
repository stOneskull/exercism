def tree_from_traversals(preorder, inorder):
    tree = {}
    if not preorder:
        return tree

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    
    root = preorder[0]
    tree["v"] = root
    root_index = inorder.index(root)
    tree["l"] = tree_from_traversals(
        preorder[1:root_index+1], inorder[:root_index]
        )
    tree["r"] = tree_from_traversals(
        preorder[root_index+1:], inorder[root_index+1:]
        )
    return tree