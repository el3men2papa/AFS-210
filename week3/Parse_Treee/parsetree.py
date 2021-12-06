import print_tree
from collections import deque

#Create a node class to store data in a parse tree
#Node should have reference links to left, right and parent 
class Node:
    def __init__ (self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

root = Node('')

#Create a function to build a parse tree from a fully parenthesized mathematical expression in infix notation.
def buildParseTree(exp):
    explist = exp.split()
    currentNode = root

    for expression in explist:
        
        #left parentheses, right parentheses, operators, and operands.
        if expression == '(':
            
            # create a node and make it the left of the currentNode
            node = Node('')
            currentNode.left = node
            
            #set the parent
            currentNode.left.parent = currentNode
            
            # then descent to that left child (ie: currentNode equal to left child)
            currentNode = currentNode.left
            
        elif expression == ')':

            # go up to the parent of the currentNode
            currentNode = currentNode.parent
            
        elif expression in '+-*/':

            # set value of the currentNode to that operator
            currentNode.val = expression
            
            # create a node and make it the right child of the currentNode
            node = Node('')
            currentNode.right = node
            
            # set the parent
            currentNode.right.parent = currentNode
            
            # then descend to that right child
            currentNode = currentNode.right

        elif expression not in '+-*/':
            
            # expression is a number
            # set value of the currentNode to that number
            currentNode.val = expression

            # go back up to our parent
            currentNode = currentNode.parent
            
        else:
            raise ValueError("Unknown Operator: " + expression)
        
#Create a function to traverse and print the parse tree in pre-order. You will need to use recursion.
def inPreOrder(node):
    # - Visit root node first
    # - Recursively do a preorder traversal of the left subtree
    # - Recursively do a preorder traversal of the right subtree
    if node:
        print(node.val)
        inPreOrder(node.left)
        inPreOrder(node.right)

#Create a function to traverse and print the parse tree in order .  You will need to use recursion.
def inOrder(node):
    # - Recursively do a inorder traversal of the left subtree
    # - Visit root node
    # - Recursively do a inorder traversal of the right subtree
    if node:
        inOrder(node.left)
        print(node.val)
        inOrder(node.right)

#Create a function to traverse and print the parse tree in post-order. You will need to use recursion.
def inPostOrder(node):
    # - Recursively do a postorder traversal of the left subtree
    # - Recursively do a postorder traversal of the right subtree
    # - Visit root node
    if node:
        inPostOrder(node.left)
        inPostOrder(node.right)
        print(node.val)

buildParseTree("( ( 11 * 2 ) + ( 10 - 2 ) )")

print_tree.print_tree(root)

print('Preorder:')
inPreOrder(root)

print('InOrder:')
inOrder(root)

print('Postorder:')
inPostOrder(root)