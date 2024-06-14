class TreeNodeDS:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_tree_from_list(elements):
    root_node = TreeNodeDS(elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNodeDS(x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

