# node structure
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
# some single linkedlist functions
class linkedlist:
    def __init__(self):
        self.head = Node()
# dispaly after by traversing linkedlist
    def display(self):
        ele = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print cur_node.data
            ele.append(cur_node.data)

# adding node from head of list
    def add_node(self,data):
        cur = self.head
        new_node = Node(data)

        while cur.next!= None:
            cur = cur.next
        cur.next = new_node
# it gives length of the linkedlist
    def length(self):
        total = 0
        p_node = self.head
        while p_node.next!=None:
            total += 1
            p_node= p_node.next
        return total

    def GetNode(self,index):
        stk = []
        if index >= self.length():
            print "error in positioning"
        else:
            curr_node = self.head
            while curr_node.next!= None:
                curr_node = curr_node.next
                stk.append(curr_node.data)

            print "the element in the given position is %d" %(stk[index])

# creating object for linked list
mylist = linkedlist()
mylist.add_node(1)
mylist.add_node(2)
mylist.add_node(3)
mylist.add_node(4)
mylist.add_node(5)
mylist.display()
mylist.GetNode(1)
# you can implement in different way but this is one of the way using linked list
