class node:
    def __init__(self,value):
        self.data = value
        self.next = None 

class stacks:
    def __init__(self):
        self.top = None

    def push (self,value):
        new_node = node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop (self):
        if self.top == None :
            print("Empty stacks")
        else:
            self.top = self.top.next

    def is_empty(self):
        return self.top == None
            
        
    def peek (self):
        print(self.top.data)
    
    def traverse(self):
        tem = self.top
        while tem != None:
            print(tem.data , end=" ")
            tem = tem.next

a = stacks()

a.push("1")
a.push("2")
a.push("3")
a.push("4")
a.push("5")
a.push("6")
a.peek()
a.pop()
a.peek()
