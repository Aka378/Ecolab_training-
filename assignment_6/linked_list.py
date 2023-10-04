class Node:
    def __init__(self, value,next_node= None,previous_node=None):
        self.value = value
        self.next = next_node
        self.previous = previous_node

class LinkedList:
    def __init__(self):
        self.first = None

    def append(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = new_node
            new_node.previous = current

    def info(self):
        if not self.first:
            return "LinkedList(empty)"
        result = "LinkedList(\t"
        current = self.first
        while current:
            result += f'{current.value}\t'
            current = current.next
        result += ")"
        return result

    def size(self):
        count = 0
        current = self.first
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
        current = self.first
        for i in range(index):
            if current:
                current = current.next
            else:
                return None
        return current.value if current else None

    def set(self, index, value):
        current = self.first
        for i in range(index):
            if current:
                current = current.next
            else:
                return False
        if current:
            current.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.first
            if self.first:
                self.first.previous = new_node
            self.first = new_node
        else:
            current = self.first
            for i in range(index - 1):
                if current:
                    current = current.next
                else:
                    return False
            if current:
                new_node.next = current.next
                new_node.previous = current
                if current.next:
                    current.next.previous = new_node
                current.next = new_node
            else:
                return False
        return True

    def remove(self, index):
        current = self.first
        for i in range(index):
            if current:
                current = current.next
            else:
                return None
        if current:
            if current.previous:
                current.previous.next = current.next
            if current.next:
                current.next.previous = current.previous
            if current == self.first:
                self.first = current.next
            return current.value
        return None
    
my_list = LinkedList()

# append elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# print the current state of the list
print("Original LinkedList:")
print(my_list.info())

# get the size of the list
print("Size of the LinkedList:", my_list.size())

#get and set values at specific indices
print("Element at index 1:", my_list.get(1))
my_list.set(1, 4)
print("Updated element at index 1:", my_list.get(1))

# insert a new element at index 1
my_list.insert(1, 5)
print("LinkedList after insertion:")
print(my_list.info())

# remove element at index 2
removed_value = my_list.remove(2)
print("Removed element:", removed_value)
print("LinkedList after removal:")
print(my_list.info())    
