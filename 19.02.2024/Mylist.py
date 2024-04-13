class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

class MyList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(data)  

    def insert(self, index, data):
        if index < 0:
            print("Index out of range")
            return
        new_node = Node(data)
        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        if current == None:
            print("List is empty")
            return
        for i in range(index - 1):                  
            if current == None:
                print("Index out of range")
                return
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def remove(self, data):
        current = self.head
        if current == None:
            print("List is empty")
            return
        if current.value == data:
            self.head = current.next_node
            return
        current = self.head
        while current.next_node:
            if current.next_node.value == data:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node
        print("Element not found in the list") 

    def pop(self, index=None):
        if self.head == None:
            print("Pop from empty list")
            return
        if index == None:
            index = -1
        if index == 0:
            popped = self.head.value
            self.head = self.head.next_node
            return popped
        current = self.head
        for i in range(index - 1):
            if current.next_node == None:
                print("Index out of range")
                return 
            current = current.next_node
        if current.next_node == None:
            return    
        popped = current.next_node.value
        current.next_node = current.next_node.next_node
        return popped 
          
    def clear(self):
        self.head = None

    def index(self, x):
        if self.head == None:
            print("Pop from empty list")
            return
        current = self.head
        index = 0
        while current:
            if current.value == x:
                return index
            current = current.next_node
            index += 1
        print("Value not found in the list")

    def sort(self):
        if self.head == None:
            print("List is empty")
            return
        new_list = []
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next_node
        new_list.sort()
        self.clear()
        for element in new_list:
            self.append(element)
            
    def reverse(self):
        if self.head == None:
            print("List is empty")
            return
        new_list = []
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next_node
        self.clear()
        for element in reversed(new_list):
            self.append(element)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

