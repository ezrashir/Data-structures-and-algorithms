# The following classes are taken from The Udemy course The Complete Data Structures and Algorithms Course in Python by Elshad Karimov

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
           
           
           
# All the additional functions in this code are my work:

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
            
   
    # My Functions:
    
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        print("CSLL created")

    def insertCSLL(self, value, location):
        if self.head is None:
            self.createCSLL(value)
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif location == -1:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode

    def traverseCSLL(self):
        if self.head is None:
            print("Empty list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self, value):
        if self.head is None:
            print("Empty list")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    print("The value does not exist")

    def deleteCSLL(self, location):
        if self.head is None:
            print("Empty list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next != self.tail:
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                inx = 0
                while inx < location - 1:
                    tempNode = tempNode.next
                    inx += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        
            
            
