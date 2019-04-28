# -*- coding:utf-8 -*-


class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.data

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")

n1.next = n2
n2.next = n3

# print(n1)
# print(n2)
# print(n3)

# print(n1.next)
# print(n2.next)
# print(n3.next)
node = n1

while node:
    print(node.data)
    node = node.next
