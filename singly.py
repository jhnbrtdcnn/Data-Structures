class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    def insert_Employee(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
            new_node.next = None

        else:
            print('head is null')

    def del_end(self):

        if self.head:
            current = self.head

            while current.next:
                pre_current = current
                current = current.next
            pre_current.next = None

        else:
            print('head is null')

    def del_beginning(self):

        if self.head:
            self.head = self.head.next
        else:
            print('head is null')


    def insert_before(self,data, search):
        found = False
        new_node = Node(data)

        if self.head:
            current = self.head
            pre_current = current
            if current.data == search:
                new_node.next = self.head
                self.head = new_node
            else:
                while current:
                    if current.data == search:
                        pre_current.next = new_node
                        new_node.next = current
                        found = True
                        break
                    pre_current = current
                    current = current.next

                if not found:
                    print('NOT FOUND')


    def insert_after(self, data, search):
        found = False
        new_node = Node(data)

        if self.head:
            current = self.head

            while current:
                if current.data == search:
                    post_current = current.next
                    current.next = new_node
                    new_node.next = post_current
                    found = True
                    break
                current = current.next

            if not found:
                print('Search value not found')

    def delete_node(self,val):
        found = False
        if self.head:
            current = self.head
            precurrent = current
            if current.data == val:
                self.head = self.head.next
            else:
                while current:
                    if current.data == val:
                        precurrent.next = current.next
                        found = True
                        break
                    precurrent = current
                    current = current.next

                if not found:
                    print('search value not found')

    def display(self):
        current = self.head

        while current:
            print(current.data, ' ', end='')
            current = current.next


l = Singly()
l.insert_Employee(4)
l.insert_Employee(2)
l.insert_Employee(8)
l.insert_Employee(9)
l.insert_Employee(10)
print('DISPLAY')
l.display()
print()
print()

print('insert end')
l.insert_end(11)
l.insert_end(12)
l.insert_end(13)

l.display()
print()
print()

print('del end')
l.del_end()
l.display()
print()
print()

print('del beginning')
l.del_beginning()
l.display()
print()
print()

print('insert before')
l.insert_before(100,9)
l.display()
print()
print()

print('insert after')
l.insert_after(200,12)
l.display()
print()
print()

print('delete node')
l.delete_node(200)
l.display()