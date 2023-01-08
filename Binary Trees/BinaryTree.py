# The following classes are taken from The Udemy course The Complete Data Structures and Algorithms Course in Python by Elshad Karimov

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return print('\n'.join(values))

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return print(nodeValue)

    def delete(self):
        self.LinkedList.head = None

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# My functions:


def MyPreOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    MyPreOrderTraversal(rootNode.leftChild)
    MyPreOrderTraversal(rootNode.rightChild)

def MyStackPreOrderTraversal(rootNode):
    stack = Stack()
    stack.push(rootNode)
    while not stack.isEmpty():
        tempNode = stack.pop()
        print(tempNode.data)
        if tempNode.rightChild:
            stack.push(tempNode.rightChild)
        if tempNode.leftChild:
            stack.push(tempNode.leftChild)
    else:
        return

def MyInOrderTraversal(rootNode):
    if rootNode is not None:
        MyInOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        MyInOrderTraversal(rootNode.rightChild)
    else:
        return

def MyPostOrderTraversal(rootNode):
    if rootNode is not None:
        MyPostOrderTraversal(rootNode.leftChild)
        MyPostOrderTraversal(rootNode.rightChild)
        print(rootNode.data)
    else:
        return

def MyLevelOrderTraversal(rootNode):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        tempNode = queue.dequeue()
        print(tempNode.data)
        if tempNode.leftChild is not None:
            queue.enqueue(tempNode.leftChild)
        if tempNode.rightChild is not None:
            queue.enqueue(tempNode.rightChild)


def FindNode(rootNode, value):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        tempNode = queue.dequeue()
        if tempNode.data == value:
            return print("Node found")
        else:
            if tempNode.leftChild is not None:
                queue.enqueue(tempNode.leftChild)
            if tempNode.rightChild is not None:
                queue.enqueue(tempNode.rightChild)
    return print("Node does not exist")

def insertNode(rootNode, newNode):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        tempNode = queue.dequeue()
        if tempNode.leftChild is not None:
            queue.enqueue(tempNode.leftChild)
        else:
            tempNode.leftChild = newNode
            return print("Node inserted")
        if tempNode.rightChild is not None:
            queue.enqueue(tempNode.rightChild)
        else:
            tempNode.rightChild = newNode
            return print("Node inserted")






# CREATING THE TREE:
Drinks = TreeNode("Drinks")

Hot = TreeNode("Hot")
Cold = TreeNode("Cold")
Drinks.leftChild = Hot
Drinks.rightChild = Cold

Tea = TreeNode("Tea")
Coffee = TreeNode("Coffee")
Hot.leftChild = Tea
Hot.rightChild = Coffee

Green = TreeNode("Green")
Black = TreeNode("Black")
Tea.leftChild = Green
Tea.rightChild = Black

Espresso = TreeNode("Espresso")
Cappuccino = TreeNode("Cappuccino")
Coffee.leftChild = Espresso
Coffee.rightChild = Cappuccino

IceTea = TreeNode("Ice Tea")
Juice = TreeNode("Juice")
Cold.leftChild = IceTea
Cold.rightChild = Juice

Peach = TreeNode("Peach")
IceTea.leftChild = Peach

Apple = TreeNode("Apple")
Orange = TreeNode("Orange")
Juice.leftChild = Apple
Juice.rightChild = Orange


# MyPreOrderTraversal(Drinks)
# MyStackPreOrderTraversal(Drinks)
# MyInOrderTraversal(Drinks)
# MyPostOrderTraversal(Drinks)
# MyLevelOrderTraversal(Drinks)

# FindNode(Drinks, "Try")
# FindNode(Drinks, "Juice")

newNode = TreeNode("Mango")
insertNode(Drinks, newNode)
MyLevelOrderTraversal(Drinks)



