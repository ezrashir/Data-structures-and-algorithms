# The following classes are taken from The Udemy course The Complete Data Structures and Algorithms Course in Python by Elshad Karimov.
# My functions use the following classes:

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
