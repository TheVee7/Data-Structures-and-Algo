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
        pass
        


