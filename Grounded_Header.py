# DECINAN, JOHNBERT
# BSIT II-B

class Node:                     # creating class Node
    def __init__(self,data):    # defining constructor for class Node
        self.data = data
        self.next = None


class Header:                   # creating class Header
    def __init__(self):         # defining constructor for the class Header
        self.data = None        # assigning the data to None
        self.next = None


class Grounded_Header:                   # creating a class Singly
    def __init__(self):         # defining constructor for class Singly
        self.head = None


    def insert_beginning(self,data):    # creating method to insert at the beginning
        head = Header()                 # creating head
        new_node = Node(data)           # creating new node

        if self.head:
            new_node.next = self.head.next  # lingking...
            self.head.next = new_node

        else:
            self.head = head
            self.head.next = new_node


    def insert_end(self,data):      # creating method to insert at the end
        new_node = Node(data)       # creating new node

        if self.head:
            current = self.head

            while current.next:     # traversing...
                current = current.next
            current.next = new_node
            new_node.next = None    # assign to None

        else:
            print('head is null')


    def del_end(self):              # creating method to delete at the end
        if self.head:
            current = self.head

            while current.next:     # traversing...
                pre_current = current
                current = current.next
            pre_current.next = None # assign to None

        else:
            print('head is null')


    def del_beginning(self):        # creating a method to delete at the beginning
        if self.head:
            self.head.next = self.head.next.next    # linking...
        else:
            print('head is null')


    def display(self):              # creating a method to display
        current = self.head

        while current:              # traversing...
            print(current.data, ' ', end='')
            current = current.next


l = Grounded_Header()                # creating an object for the class Singly
print('Insert beginning')
l.insert_beginning(4)       # calling Insert_beginning method with data being passed
l.insert_beginning(2)       # calling Insert_beginning method with data being passed
l.insert_beginning(8)       # calling Insert_beginning method with data being passed
l.insert_beginning(9)       # calling Insert_beginning method with data being passed
l.display()                 # calling method display
print()
print()

print('Insert end')
l.insert_end(11)            # calling Insert_end method with datas being passed...
l.insert_end(1)
l.display()
print()
print()

print('Delete beginning')
l.del_beginning()           # calling del_beginning method
l.display()
print()
print()

print('Delete end')
l.del_end()                 # calling del_end method
l.display()
print()