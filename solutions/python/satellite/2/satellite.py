def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    
    return make_tree(preorder, inorder)
    

def make_tree(preorder, inorder):
    tree = {}
    if not preorder:
        return tree
   
    root = preorder[0]
    root_index = inorder.index(root)
    tree["v"] = root
    tree["l"] = make_tree(preorder[1:root_index+1], inorder[:root_index])
    tree["r"] = make_tree(preorder[root_index+1:], inorder[root_index+1:])
    
    return tree