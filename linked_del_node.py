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
    
    def del_node(self,node_key):
        if self.head == None:
            return

        head_value = self.head.data
        if head_value == node_key:
            self.head = self.head.next
            return
        
        node = self.head
        # pre = node
        while node:
            if node.data == node_key:
                node = node.next
                pre.next = node
                return
            pre = node
            node = node.next

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n1.next = n2
n2.next = n3

list = LinkedList()            
list.head = n1
print("删除前：")
list.print_list()

print("-"*50)
print("删除后：")
list.del_node("3")

list.print_list()

            
