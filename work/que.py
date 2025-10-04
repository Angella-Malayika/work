print("Nakanwagi Angella \n")
print("Reg.no:2024-B071-21804 \n")

class Queue:
    def __init__(self):
        self.items = []            # List to hold queue elements

    def enqueue(self, item):
        #Add an item to the back of the queue.
        self.items.append(item)

    def dequeue(self):
        #Remove and return the item from the front of the queue.
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        #Return the front item without removing it.
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        #Check if the queue is empty.
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def show(self):
        """Display all items in the queue."""
        print("Queue:", self.items)

#  Using the queue
q = Queue()

#  names in the equeue
q.enqueue("Angella")
q.enqueue("Mary")
q.enqueue("Claire")
q.enqueue("Rose")
q.enqueue("Mildred")
q.enqueue("Malaika")

print(" Queue list:")
q.show()
# Remove the first item
removed = q.dequeue()
print("\nDequeued:", removed)
#  Add Jose
q.enqueue("Jose")
print("After adding Jose:")
q.show()
# view the top element
print("Front item:", q.peek())
#check if the queue is empty 
print("Is empty?", q.is_empty())
#check the len of the queue
print("Size:", q.size())
