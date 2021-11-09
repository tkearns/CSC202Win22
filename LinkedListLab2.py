class node:
    def __init__(self, initValue):
        self.value = initValue
        self.next = None

    def setData(self, value):
        self.value = value

    def getData(self):
        return self.value

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, newvalue):
        temp = node(newvalue)
        temp.setNext(self.head)
        self.head = temp

    def append(self, newvalue):  #check if it works on empty list????
        current = self.head
        previous = self.head    # allows for list to be empty
        while current != None:  # finds last node in list stores it in previous
            previous=current
            current = current.getNext()
        previous.setNext(node(newvalue))


    def top(self):
        return self.head.getData()   # self.head has value a node and thus can use getData method

    def pop(self):
        if self.isEmpty():
            return None   # this should raise an exception or be as assert
        else:
            temp = self.head.getData()
            self.head = self.head.getNext()
            return temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def sum(self):
        current = self.head
        total = 0
        while current != None:
            total = total + current.getData()
            current = current.getNext()
        return total

stack = linkedList()
stack.insert(2)
stack.insert(4)
stack.insert(6)
stack.insert(8)
stack.append(10)
print(stack.top())
print("Size=" + str(stack.size()) )
print("Sum=" + str(stack.sum()))
print(stack.isEmpty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())

