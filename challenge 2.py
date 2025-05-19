class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(postfix):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in postfix:
        if token not in operators:
            # If token is an operand, create a leaf node and push it to stack
            stack.append(Node(token))
        else:
            # If token is an operator, pop two nodes and make them children
            right = stack.pop()
            left = stack.pop()
            node = Node(token)
            node.left = left
            node.right = right
            stack.append(node)
    # The last node on the stack is the root of the expression tree
    return stack.pop()
# ✅ Test cases
# Test 1: Simple addition
# Input: 2 3 +
# Tree:    +
#         / \
#        2   3
tokens1 = ['2', '3', '+']
tree1 = build_expression_tree(tokens1)
print(tree1.value == '+' and tree1.left.value == '2' and tree1.right.value == '3')  # 🌱 Simple tree

# Test 2: Complex expression
# Input: 2 3 4 * +
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tokens2 = ['2', '3', '4', '*', '+']
tree2 = build_expression_tree(tokens2)
print(tree2.value == '+' and tree2.left.value == '2' and tree2.right.value == '*')  # 📊 Operator precedence

# Test 3: Nested operations
# Input: 1 2 + 3 4 - *
# Tree:    *
#         / \
#        +   -
#       / \ / \
#      1  2 3  4
tokens3 = ['1', '2', '+', '3', '4', '-', '*']
tree3 = build_expression_tree(tokens3)
print(tree3.value == '*' and tree3.left.value == '+' and tree3.right.value == '-')  # 🔗 Nested operations

# Test 4: Expression with variables
# Input: a b c * +
# Tree:    +
#         / \
#        a   *
#           / \
#          b   c
tokens4 = ['a', 'b', 'c', '*', '+']
tree4 = build_expression_tree(tokens4)
print(tree4.value == '+' and tree4.left.value == 'a' and tree4.right.value == '*')  # 🔤 Variable tree

# Test 5: More complex expression
# Input: a b + c d - /
# Tree:    /
#         / \
#        +   -
#       / \ / \
#      a  b c  d
tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
tree5 = build_expression_tree(tokens5)
print(tree5.value == '/' and tree5.left.value == '+' and tree5.right.value == '-')  # 🧮 Complex tree
