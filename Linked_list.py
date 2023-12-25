class node:
    def __init__(self,value):
        self.data = value
        self.next = None
class linked:
    def __init__(self):
        self.head = None
        self.n = 0 

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
        
    def insert(self,value):
        new_node = node(value)
        if self.n == 0 :
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.n = self.n + 1

    def _append (self,value):
        new_node = node(value)
        if self.n == 0 :
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None :
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1
        
    def insert_after(self,after,value):
        new_node = node(value)
        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr !=  None :
            new_node.next = curr.next 
            curr.next = new_node
            self.n += self.n
        else:
            print("Item not found")

    def clear(self):
        self.head = None
        self.n = 0



l = linked()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
print(l)
l.insert_after(3,69)
l.insert_after(69,79)
print(l)
l.clear()
print(l)
print(11)






