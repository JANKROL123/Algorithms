class Node:
    def __init__(self,x):
        self.key = x
        self.next = None
        self.prev = None
class LinkedList:
    def ListLast(self):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        return curr_node
    def __init__(self):
        self.none = Node(None)
        self.head = self.none
        last = self.ListLast()
        self.head.prev = last
        last.next = self.head
    def ListPrint(self):
        curr_node = self.head
        print(curr_node.key)
        curr_node = curr_node.next
        while curr_node.key != None:
            print(curr_node.key)
            curr_node = curr_node.next
    def ListInsert(self,x):
        if self.head.next != None:
            x.next = self.head.next
            self.head.next.prev = x
        self.head.next = x
        x.prev = self.head
    def ListSearch(self,k):
        x = self.head.next
        while x.key != None and x.key != k:
            x = x.next
        return x.key
    def ListDelete(self,x):
        x.prev.next = x.next
        x.next.prev = x.prev
    def ListDuplicate(self):
        x = self.head.next
        while x.key != None:
            y = x.next
            while y.key != None:
                if y.key == x.key:
                    self.ListDelete(y)
                y = y.next
            x = x.next
    def ListScal(self,L2):
        y = L2.head.next
        while y.key != None:
            z = Node(y.key)
            self.ListInsert(z)
            y = y.next
# elements to be inserted to list (polish names)
a = Node("ala")
b = Node("ala")
c = Node("jan")
d = Node("wojciech")
e = Node("krzysztof")
f = Node("agata")
g = Node("wojciech")
h = Node("martyna")
i = Node("jan")
j = Node("krzysztof")
# 2 lists
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
# filling linked_list_1
linked_list_1.ListInsert(a)
linked_list_1.ListInsert(b)
linked_list_1.ListInsert(c)
linked_list_1.ListInsert(d)
linked_list_1.ListInsert(e)
# filling linked_list_2
linked_list_2.ListInsert(f)
linked_list_2.ListInsert(g)
linked_list_2.ListInsert(h)
linked_list_2.ListInsert(i)
linked_list_2.ListInsert(j)
# checking how function ListSearch works 
print(linked_list_1.ListSearch("jan"))
print(linked_list_2.ListSearch("wiktor"))
print()
# checking how function ListScal works
linked_list_1.ListScal(linked_list_2)
linked_list_1.ListPrint()
print()
# checking how function ListDuplicate works
linked_list_1.ListDuplicate()
linked_list_1.ListPrint()
