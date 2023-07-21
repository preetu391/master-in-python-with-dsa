class Node:
    def __init__(self, data= None,  next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_ll_values(self):
        n = self.head
        if n is None:
            print("Linked list is empty")
            return
        print()
        while n is not None:
            print(n.data, end="--> ")
            n=n.next

    def insert_in_end(self,data):
        n = self.head
        while n.next is not None:
            n= n.next
        node = Node(data)
        n.next=node

    def insert_after_a_node(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print("Node not found, cannot insert!")
            return
        node = Node(data, n.next)
        n.next = node

    def remove_from_beginning(self):
        if self.head is None:
            print("Linked list is empty, cannot remove!")
            return
        self.head= self.head.next

    def remove_from_end(self):
        if self.head is None:
            print("Linked list is empty, cannot remove!")
            return
        n = self.head
        while n.next.next is not None:
            n=n.next
        n.next = None  

    def remove_specific_node(self,s):
        if self.head is None:
            print("Linked list is empty, cannot remove!")
            return
        n = self.head
        while n is not None:
            if n.next.data == s:
                break
            n = n.next
        if n is None:
            print("Node not found!, so cannot remove")
            return
        n.next = n.next.next


ll = LinkedList()
ll.insert_in_beginning(2)
ll.insert_in_beginning(5)
ll.insert_in_end(6)
ll.insert_in_end(1)
ll.insert_after_a_node(7,6)
ll.remove_from_beginning()
ll.remove_from_end()
ll.insert_in_end(8)
ll.insert_in_end(3)
ll.remove_specific_node(8)
ll.print_ll_values()
    

