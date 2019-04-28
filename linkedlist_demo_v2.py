# -*- coding:utf-8 -*-

class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        node1 = self.head
        while node1:
            print(node1.data)
            node1 = node1.next

list1 = LinkedList()
n1 = Node("1")
n2 = Node("2")
n3 = Node("3")

n1.next = n2
n2.next = n3

list1.head = n1

list1.print_list()
