import re

# Complete this list if you need more operator
binaryOperator = ["mul", "add", "sub", "protected_div"]
unaryOperator = ["protected_log", "neg", "cos", "sin"]


# If you add an operator add the associated token that you want in your result expression here
def value_to_token(value):
    if value == "mul":
        return '*'
    elif value == "add":
        return '+'
    elif value == "sub":
        return '-'
    elif value == "protected_div":
        return '/'
    elif value == "protected_log":
        return "log"
    elif value == "neg":
        return '-'
    elif value == "cos":
        return "cos"
    elif value == "sin":
        return "sin"


# Class that represent a node in a binary tree with a right and left son
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.isLeftNode = False  # boolean used to find the right son of a node


# transforms a complex expression to a list
# ie mul(add(1,2),3) => [mul,add,1,2,3]
def simplify(expression):
    expression = expression.replace("(", " ")
    expression = expression.replace(")", " ")
    expression = expression.replace(",",  " ")
    expression = re.sub(' +', ' ', expression)
    if expression[len(expression)-1] == ' ':
        expression = expression[:-1]
    expression = expression.split(' ')
    return expression


# take an expression list and return a list containing each node of the expression tree with the value of each son
# /!\ nodes are not linked together
def get_node_list(expression_list):
    node_list = []
    for i, operator in enumerate(expression_list):
        if operator in binaryOperator:
            node = Node(operator, None, None)  # We create a new node that will be stored in our list
            node.left = expression_list[i+1]  # The next element in the list is always the left son of the current node
            # We now try to find the right son of our node
            if expression_list[i+1] in unaryOperator:
                count = 1
            elif expression_list[i+1] in binaryOperator:
                count = 2
            else:
                count = 0
            j = i+2

            while count > 0:
                # if we find a binary operator we know that there are 2 element that comes before our node right son
                if expression_list[j] in binaryOperator:
                    count += 2
                # Same as the binary operator but with only 1 element
                elif expression_list[j] in unaryOperator:
                    count += 1
                count -= 1
                j += 1
            # we found the value of our right son, we complete our node and add it to the list
            node.right = expression_list[j]
            node_list.append(node)
        elif operator in unaryOperator:
            # since an unary operator as only one son we already know that it'll be the next one in the list
            node = Node(operator, None, None)
            node.left = expression_list[i+1]
            node_list.append(node)
    return node_list


# Return the root of our expression Tree
def get_tree_root(expression):
    node_list = get_node_list(simplify(expression))
    # now we link node son to other node
    # we start with the left one
    for i, node in enumerate(node_list):
        # if the 
        if node.left in unaryOperator or node.left in binaryOperator:
            node.left = node_list[i + 1]
            node.left.isLeftNode = True

    # then the right one
    for i, node in enumerate(node_list):
        if node.right in unaryOperator or node.right in binaryOperator:
            j = i + 1
            while node_list[j].isLeftNode:  # the next node that is not a left son will be our right son
                j += 1
            node.right = node_list[j]

    return node_list[0]


# Start from the root and recursively parse our tree to recreate the final expression
def parse_tree(node):
    result = ""
    if isinstance(node, Node):
        if node.value in binaryOperator:
            result = "({}{}{})".format(parse_tree(node.left), value_to_token(node.value), parse_tree(node.right))
        elif node.value in unaryOperator:
            result = value_to_token(node.value) + "({})".format(parse_tree(node.left))
    else:
        result = str(node)
    return result


def get_result_expression(expression):
    root = get_tree_root(expression)
    return parse_tree(root)
