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
        
    def tail_insert(self,new_data):
        new_data = Node(new_data)
        node = self.head
        if node is None:
            self.head = new_data
            return
        
        last_node = node.next
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_data

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
list.tail_insert("4")

list.print_list()
