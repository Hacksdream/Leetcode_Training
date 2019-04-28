# -*- coding:utf-8 -*-

class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def head_insert(self,newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n1.next = n2
n2.next = n3

list = LinkedList()            
list.head = n1
print("插入前：")
list.print_list()

print("-"*50)
print("插入后：")
list.head_insert("0")

list.print_list()
