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

    def mid_insert(self,mid_node,new_data):
        if mid_node is None:
            print("This node is not exist!")
            return
        
        new_node = Node(new_data)
        new_node.next = mid_node.next
        mid_node.next = new_node

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
list.mid_insert(n2,"4")

list.print_list()