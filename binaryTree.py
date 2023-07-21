import queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    def insert_left(self,data):
        if self.left_child == None:
            self.left_child = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.left_child = self.left_child
            self.left_child = new_node
    def insert_right(self,data):
        if self.right_child == None:
            self.right_child = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.right_child = self.right_child
            self.right_child = new_node
    def pre_order(self):
        print(self.data)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.data)
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.data)

    def bfs(self):
        queue1 = queue.Queue()
        queue1.put(self)
        while not queue1.empty():
            curr_node = queue1.get()
            print(curr_node.data)
            if curr_node.left_child:
                queue1.put(curr_node.left_child)
            if curr_node.right_child:
                queue1.put(curr_node.right_child)

node_1 = BinaryTree(1)
node_1.insert_left(2)   #created left child of 1 node
node_1.insert_right(3)

node_2 = node_1.left_child #binding the left child of 1 node to 2 node to be used further
node_2.insert_left(4)
node_3 = node_1.right_child
node_3.insert_left(5)

node_4 = node_2.left_child
node_5 = node_3.left_child
node_5.insert_right(6)
node_6 = node_5.right_child

node_1.bfs()

