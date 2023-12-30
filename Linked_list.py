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

    def delete_head(self):
        # curr = self.head
        if self.n == 0 :
            print("EMPTY linked list..")
        else:
            self.head = self.head.next
        self.n = self.n + 1

    def del_tail(self):
        curr = self.head
        if self.n == 0:
            print("this ll is empty")
        
        if curr.next == None :
            return self.delete_head
        
            
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n + 1


    def remove (self,value):
        if self.head == None :
            print("I think ll is empty")
            return
        
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head
        while curr.next != None :
            if curr.next.data == value :
                break
            curr = curr.next
            
        if curr.next == None :
            print('item not found')
        else :
            curr.next = curr.next.next
            self.n =  self.n - 1
        
    def search_value(self,value):
        curr = self.head
        pos = 0 
        while curr != None:
            if curr.data == value:
                print(pos)
            curr = curr.next
            pos = pos + 1

    def search_index(self,item):
        curr = self.head
        pos = 0 
        while curr != None:
            if pos == item:
                print(curr.data)
            curr = curr.next
            pos = pos + 1




l = linked()
l._append(1)
l._append(2)
l._append(3)
l._append(4)
l._append(5)
print(l)
            
l.search_index(3)
l.search_index(1)




            



    



