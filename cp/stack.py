# dynamic stack operation
class Stack(object):
    def __init__(self, limit=10):
        self.stk = limit*[]
        self.limit = limit

    def is_empty(self):
        return self.stk <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            print("stack is full")
            print("stack is resize")
            self.resize()

        else:
            self.stk.append(item)
            print("The pushed element to stack is %s" % self.stk[-1])

    def peek(self):
        if len(self.stk) <= 0:
            print("stack is underflow")

        else:
            print("The top most element in current stack is %s" % self.stk[-1])

    def size(self):
        print("The length of the stack is %s" % len(self.stk))

    def pop(self):
        if len(self.stk) <= 0:
            print("stack underflow")
            return 0
        else:
            print("The deleted element from stack is %s" % self.stk.pop())

    def resize(self):
        newstk = list(self.stk)
        self.limit = 2*self.limit
        self.stk = newstk


our_stack = Stack()
our_stack.push('3')
our_stack.push('3')
our_stack.push('4')
our_stack.push('5')
our_stack.push('6')
our_stack.size()
our_stack.peek()
our_stack.push('7')
our_stack.push('8')
our_stack.push('9')
our_stack.push('10')
our_stack.push('11')
our_stack.push('1')
our_stack.pop()
our_stack.pop()
our_stack.peek()
our_stack.size()

'''stack is one of the popular data structures
this is one of the way to implement'''


