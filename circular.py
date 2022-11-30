class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head
            self.head = self.tail.next = node

        else:
            self.head = self.tail = node

    def insert_end(self, data):
        node = Node(data)

        if self.head:
            self.tail.next = self.tail = node
            node.next = self.head
        else:
            self.head = self.tail = node


    def del_beginning(self):

        if self.head:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            print('the list is null')

    def del_end(self):
        if self.head:
            current = self.head
            while current.next != self.head:
                precurrent = current
                current = current.next
            self.tail = precurrent
            self.tail.next  = self.head



    def insert_before(self, data, val):
        node = Node(data)

        if self.head:
            current = self.head
            precurrent = current

            while current.data != val:
                precurrent = current
                current = current.next

            if precurrent == self.head:
                self.tail.next = node
                node.next = self.head
                self.head = node
            else:
                precurrent.next = node
                node.next = current

        else:
            self.head  = self.tail = node
            self.head.next = self.head

    def insert_after(self, data, val):
        node = Node(data)

        if self.head:
            current = self.head
            post_current = current.next

            while current.data != val:
                current = current.next
                post_current = current.next

            if current == self.tail:
                self.tail.next = node
                node.next = self.head
            else:
                current.next = node
                node.next = post_current
        else:
            self.tail = self.head = node
            self.tail.next = node

    def del_node(self, data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            while current.next != self.head:
                postcurrent = current.next
                precurrent = current
                if postcurrent.data == data:
                    if postcurrent == self.tail:
                        self.tail = precurrent
                        self.tail.next = self.head
                    else:
                        current.next   = postcurrent.next
                        break
                current = current.next


    def display(self):

        if self.head:
            current = self.head

            while current.next != self.head:
                print(current.data, end=' ')
                current = current.next

            print(current.data)
        else:
            print("list is null")

        print("head:", self.head.data)
        print("tail:", self.tail.data)


c = Circular()
print('insert before')
c.insert_before(100,12)
c.display()
print()

print('insert after')
c.insert_after(1000,9)
c.display()
print()
print('insert beginning')
c.insert_beginning(10)
c.insert_beginning(11)
c.insert_beginning(12)
c.insert_beginning(13)
c.display()
print()
print('delete beginning')
c.del_beginning()
c.display()
print()
print('insert end')
c.insert_end(9)
c.insert_end(8)
c.display()
print()

print('delete end')
c.del_end()
c.display()
print()


print('insert before')
c.insert_before(100,12)
c.display()
print()

print('insert after')
c.insert_after(1000,9)
c.display()
print()

print('DELTE NODE')
c.del_node(1000)
c.display()
print()

