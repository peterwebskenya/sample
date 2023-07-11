class base:
    def __init__(self,a,c,d,e):
        self.a = "i have rights"
        self.__c = "and priviledges"
        self.d = "more rights"
        self.e = "and power"
class derived(base):
    def __init__(self):
        print(self.a) #accessible
        print(self.__c) #unaccessible
        print(self.d) #accessible
        print(self.e) #accessible

#create an instance of parent class
obj1 = base('a','c','d','e')
print(obj1.a)
#print(obj1.c)
print(obj1.d)
print(obj1.e)