class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQ:
    # Create an empty linked queue.
    def __init__(self):
            self.first = None
            self.last = None

    def enqueue(self, data):
        # Meaning the linked queue is empty.
        if self.first is None:
            # Sets the first node to both first and last in the linked queue.
            self.first = Node(data)
            self.last = self.first
        else:
            # Sets the previous node's next to the node
            self.last.next = Node(data)
            # Sets the last one to the node.
            self.last = self.last.next

    def dequeue(self):
        # Check if there is a linked queue.
        if self.first is None:
            return None
        else:
            # Used to showcase what is being removed.
            to_return = self.first.data
            # Set's the first to the next one which means the node of the next one.
            self.first = self.first.next
            return to_return

    def isEmpty(self):
        return self.first is None

    def size(self):
        position = self.first
        number = 0
        while position is not None:
            number = number + 1
            position = position.next
        return number
