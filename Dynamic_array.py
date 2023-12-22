import ctypes
class meralist:
    def __init__(self):
        self.size = 1 
        self.n = 0 
        self.a = self.__make_array(self.size)
    
    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.a[self.n] = item
        self.n = self.n + 1
    
    def __resize(self,new_capa):
        b = self.__make_array(new_capa)
        self.size = new_capa
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result  + self.a[i] + ","
        return '[' + result[:-1] + ']'
    
 
    def __getitems__(self,index):
        if 0 >= index >= self.n:
            return self.a[index]
        else:
            print("type error")

    def clear (self):
        self.n = 0
        self.size = 1 

    def find(self,item):
        for i in range(self.n):
            if self.a[i] == item :
                return i
            else:
                print("type error")
        
    def del_pos (self,pos):
        if 0 <= pos <= self.n :
            for i in range(pos,self.n-1):
                self.a[i] = self.a[i+1]
            self.n = self.n - 1
        else :
            print("error")

    def _pop (self):
        if self.n == 0 :
            print('list is empty')

        self.n = self.n - 1
        print(self.n)


    def _remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.del_pos(pos)
        else:
            print('Kuch to error h varun bhaiya ji')
            print(pos)
            

    
    
s = meralist()
s.append('2')
s.append('21')
s.append('21')
s.append('21')
s.append('21')
print(s)