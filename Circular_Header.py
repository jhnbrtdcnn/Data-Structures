# DECINAN, JOHNBERT
# BSIT II-B

class Node:                     # creating class Node
    def __init__(self, data):   # defining constructor for class Node
        self.data = data
        self.next = None

class Header:               # creating class Header
    def __init__(self):     # defining constructor for class Header
        self.data = None    # assigning the data to None
        self.next = None


class Circular_Header:      # creating class Circular_Header
    def __init__(self):     # defining constructor
        self.head = None
        self.tail = None

    def insert_beginning(self, data):   # creating a method to insert at the beginning
        head = Header()                 # creating head
        node = Node(data)               # creating node

        if self.head:
            node.next = self.head.next  # linking...
            self.head.next = node
            self.tail.next = self.head


        else:                           # else body executed if the list is empty
            self.head  = head           # linking...
            self.tail = self.head.next  = node

    def insert_end(self, data):         # creating mehtod to insert at the end
        node = Node(data)               # creating node

        if self.head:
            self.tail.next = self.tail = node   # linking...
            node.next = self.head
        else:                           # else body executed if the list is empty
            self.head = self.tail = node


    def del_beginning(self):            # creating a method to delete at the beginning

        if self.head:
            self.head.next = self.head.next.next    # linking...
            self.tail.next = self.head
        else:
            print('the list is null')

    def del_end(self):              # creating a method to delete at the end
        if self.head:
            current = self.head
            while current.next != self.head:    # traversing...
                precurrent = current            # lingking...
                current = current.next
            self.tail = precurrent
            self.tail.next  = self.head

    def display(self):              # creating a method to display the list

        if self.head:
            current = self.head

            while current.next != self.head:    # traversing...
                print(current.data, end=' ')
                current = current.next

            print(current.data)
        else:
            print("list is null")



c = Circular_Header()       # creating object of the class Circular_Header

print('Insert beginning')
c.insert_beginning(10)      # calling insert_beginning method with datas being passed...
c.insert_beginning(11)
c.insert_beginning(12)
c.insert_beginning(13)
c.display()                 # calling display method to display the list...
print()

print('Delete Beginning')
c.del_beginning()           # calling del_beginning method...
c.display()
print()

print('Insert end')
c.insert_end(15)            # calling insert_end method...
c.insert_end(13)
c.display()
print()

print('Delete end')
c.del_end()                 # calling del_end method...
c.display()


