# max heap which pre locates up and down as per requirements

class MaxHeap:

    def __init__(self, items = []):
        self.heaplist = [0]
        self.size = 0
        for i in items:
            self.heaplist.append(i)

    def push(self, data):
        self.heaplist.append(data)
        self.prelocateup(len(self.heaplist)-1)

    def peek(self):
        if self.heaplist[1]:
            print(self.heaplist[1])
        else:
            print('False')

    def pop(self):
        if len(self.heaplist) > 2:
            self.swap(1, len(self.heaplist) - 1)
            max = self.heaplist.pop()
            self.prelocatedown(1)
        elif len(self.heaplist) == 2:
            max = self.heaplist.pop()
        else:
            max = False

        print (max)

    def swap(self, i, j):
        self.heaplist[i], self.heaplist[j] = self.heaplist[j], self.heaplist[i]

    def prelocateup(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heaplist[index] > self.heaplist[parent]:
            self.swap(index, parent)
            self.prelocateup(parent)

    def prelocatedown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heaplist) > left and self.heaplist[largest] < self.heaplist[left]:
            largest = left
        if len(self.heaplist) > right and self.heaplist[largest] < self.heaplist[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.prelocatedown(largest)



m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heaplist[1:len(m.heaplist)]))
m.peek()
m.pop()
print("after poping element")
m.peek()

