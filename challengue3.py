from dataclasses import dataclass

@dataclass
class Node:
    value: str               # '+', '-', '*', '/', or an integer as string
    left:  'Node' = None
    right: 'Node' = None

def evaluate_expression_tree(root: Node) -> int | float:
    if root is None:
        raise ValueError("Empty tree")

    # Leaf node → operand
    if root.left is None and root.right is None:
        return int(root.value)

    # Internal node → operator
    left_val  = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    match root.value:
        case '+': return left_val + right_val
        case '-': return left_val - right_val
        case '*': return left_val * right_val
        case '/':
            return left_val // right_val if left_val % right_val == 0 else left_val / right_val
        case _:
            raise ValueError(f"Unsupported operator {root.value!r}")
# Test 1: 2 + 3 = 5
node1 = Node('+', Node('2'), Node('3'))
print(evaluate_expression_tree(node1) == 5)

# Test 2: 4 * 5 = 20
node2 = Node('*', Node('4'), Node('5'))
print(evaluate_expression_tree(node2) == 20)

# Test 3: 2 + (3 * 4) = 14
node3 = Node('+', Node('2'), Node('*', Node('3'), Node('4')))
print(evaluate_expression_tree(node3) == 14)

# Test 4: 8 / 4 = 2
node4 = Node('/', Node('8'), Node('4'))
print(evaluate_expression_tree(node4) == 2)

# Test 5: (1 + 2) * (8 - 3) = 15
node5 = Node('*',
             Node('+', Node('1'), Node('2')),
             Node('-', Node('8'), Node('3')))
print(evaluate_expression_tree(node5) == 15)
