# The following classes are taken from The Udemy course The Complete Data Structures and Algorithms Course in Python by Elshad Karimov


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
           
           
           
All the additional functions in this code are my work:

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
     
    # My Functions:
    
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        print("DLL created")
        
    def insertDLL(self, location, nodeValue):
        node = Node(nodeValue)
        if self.head is None:
            print('Must first create list')
        else:
            if location == 0:
                node.prev = None
                self.head.prev = node
                node.next = self.head
                self.head = node
            elif location == -1:
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                inx = 0
                while inx < location - 1:
                    tempNode = tempNode.next
                    inx += 1
                node.next = tempNode.next
                node.prev = tempNode
                node.next.prev = node
                tempNode.next = node
                
    def traverseDLL(self):
        if self.head is None:
            print ("Empty list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                
    def reverseTraversalDLL(self):
        if self.tail is None:
            print("Empty list")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                
    def searchDLL(self, nodeValue):
        if self.head is None:
            print("Empty list")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return print("Node value found: " + str(tempNode.value))
                tempNode = tempNode.next
            return print("Node doesn't exist")
            
    def deleteNodeDLL(self, location):
        if self.head is None:
            return print("Empty list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                inx = 0
                while inx < location - 1:
                    tempNode = tempNode.next
                    inx += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
                
    def deleteEntireDLL(self):
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None
            
