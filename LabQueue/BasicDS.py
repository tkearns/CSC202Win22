class Queue:    # cheating using built in operations inefficient - want both linked and circular list implementations
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# class PriorityQueue:   #implement as an ordered list more efficient implementations come later
