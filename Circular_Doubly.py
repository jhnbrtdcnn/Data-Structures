# DECINAN, JOHNBERT
# BSIT II-B

class Node:     # creating class Node
    def __init__(self,data):    # defining constructor for class Node
        self.prev = None
        self.data = data
        self.next = None

class Circular_Doubly:      # creating class Circular_Doubly
    def __init__(self):     # defining constructor for the class
        self.head = None
        self.tail = None

    def insert_beginning(self,data):    # creating  method to insert at the beginning
        node = Node(data)               # creating new node
        if self.head:
            node.next = self.head       # linking...
            self.head.prev = node
            self.head = node
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            self.head = self.tail = node

    def delete_beginning(self):         # creating method to delete at the beginning
        if self.head:
            self.head = self.head.next  # linking...
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            print('Head is Null')

    def insert_end(self,data):          # creating method to insert at the end
        node = Node(data)               # creating new node
        if self.head:
            self.tail.next = node       # linking...
            node.prev = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            self.head = self.tail = node

    def delete_end(self):               # creating a method to delete at the end
        if self.head:
            self.tail = self.tail.prev  # linking...
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            print('Head is Null')

    def display(self):                       # creating a method to display
        if self.head:
            current = self.head
            while current.next != self.head: # traversing...
                print(current.data, end='  ')
                current = current.next

            print(current.data)

    def display_reverse(self):          # creating amethod to display in reverse order
        if self.head:
            current = self.tail
            while current != self.head: # traversing...
                print(current.data , end = '  ')
                current = current.prev

            print(current.data)

        else:
            print('Head is Null')

    def even(self):                       # creating a method to display the even numbers
        if self.head:
            current = self.head
            while current.next != self.head:    # traversing...
                if current.data %2 == 0:        # checking if the number is even
                    print(current.data, end='  ')

                current = current.next

            if current.data %2 == 0:
                print(current.data, end='   ')

        else:
            print('Empty List')

    def odd(self):                          # creating a method to display the odd numbers
        if self.head:
            current = self.head
            while current.next != self.head:    # traversing...
                if current.data % 2 != 0:       # checking if the number is odd
                    print(current.data, end='  ')

                current = current.next

            if current.data % 2 != 0:
                print(current.data, end='   ')

        else:
            print('Empty List')



c = Circular_Doubly()      # creating object for the class Circular_Doubly
print('Insert Beginning')
c.insert_beginning(10)     # calling insert_beginning method with data being passed
c.insert_beginning(9)      # calling insert_beginning method with data being passed
c.insert_beginning(8)      # calling insert_beginning method with data being passed
c.insert_beginning(4)      # calling insert_beginning method with data being passed
c.display()                # calling display method
print()
print('Insert End')
c.insert_end(11)           # calling insert_end method with data being passed
c.insert_end(13)           # calling insert_end method with data being passed
c.display()
print()
print('Delete Beginning')
c.delete_beginning()       # calling delete_beginning method
c.display()
print()
print('Delete End')
c.delete_end()             # calling delete_end method
c.display()
print()
print('Reverse order')
c.display_reverse()        # calling a method to display in reverse order
print()


print('EVEN')
c.even()                   # calling even method to print the even numbers
print()
print()
print('ODD')
c.odd()                    # calling odd method to print the odd numbers
print()
print()
print('Display List')
c.display()                # calling again the display method to display the list




