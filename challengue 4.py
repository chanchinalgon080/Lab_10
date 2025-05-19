from dataclasses import dataclass

@dataclass
class Node:
    value: str
    left:  'Node' = None
    right: 'Node' = None

def inorder_traversal(root: Node) -> list[str]:
    """Inorder traversal: left, root, right"""
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def preorder_traversal(root: Node) -> list[str]:
    """Preorder traversal: root, left, right"""
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root: Node) -> list[str]:
    """Postorder traversal: left, right, root"""
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# Test 1
node1 = Node('+', Node('2'), Node('3'))
print(inorder_traversal(node1) == ['2', '+', '3'])   
print(preorder_traversal(node1) == ['+', '2', '3'])  
print(postorder_traversal(node1) == ['2', '3', '+'])

# Test 2
node2 = Node('+', Node('*', Node('2'), Node('3')), Node('5'))
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])   
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])  
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])

# Test 3
node3 = Node('X')
print(inorder_traversal(node3) == ['X'])   
print(preorder_traversal(node3) == ['X'])  
print(postorder_traversal(node3) == ['X'])

# Test 4
print(inorder_traversal(None) == [])   
print(preorder_traversal(None) == [])  
print(postorder_traversal(None) == [])

# Test 5
node5 = Node('/',
             Node('+', Node('a'), Node('b')),
             Node('-', Node('c'), Node('d')))
print(inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'])   
print(preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'])  
print(postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/'])
