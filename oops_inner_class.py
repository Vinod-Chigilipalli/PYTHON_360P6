'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is display method")
    class inner1:
        a,b,c=10,20,30
        @classmethod
        def display(cls):
            print("this is class method from inner class")
        @staticmethod
        def display2():
            print("this is static emthod from inner class")
        def display3(self):
            print("this is instance method from inner class")
s1=sample()
s1.display()
i1=s1.inner1()
print(i1.a,i1.b,i1.c)
i1.display()
i1.display2()
i1.display3()
'''
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is class method")
    class inner1:
        a,b,c=10,20,30
        @classmethod
        def display(cls):
            print(sample.x,sample.y,sample.z)
            print(cls.a,cls.b,cls.c)
            print("this is class method from innner")
        @staticmethod
        def display2():
            print(sample.x,sample.y,sample.z)
            print(sample.inner1.a,sample.inner1.b,sample.inner1.c,)
            print("this is static emthod from inner class")
        def display3(self):
            print(sample.x,sample.y,sample.z)
            print(self.a,self.b,self.c)
            print("this is instance method from inner class")
s1=sample()
s1.display()
i1=s1.inner1()
print(i1.a,i1.b,i1.c)
i1.display()
i1.display2()
i1.display3()
'''
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is class method")
    class inner1:
        a,b,c=10,20,30
        def __init__(self,a1,b1,c1):
            self.a1,self.b1,self.c1=a1,b1,c1
        @classmethod
        def display(cls):
            print(sample.x,sample.y,sample.z)
            print(cls.a,cls.b,cls.c)
            print("this is class method from innner")
        @staticmethod
        def display2():
            print(sample.x,sample.y,sample.z)
            print(sample.inner1.a,sample.inner1.b,sample.inner1.c,)
            print("this is static emthod from inner class")
        def display3(self):
            print(sample.x,sample.y,sample.z)
            print(self.a,self.b,self.c)
            print(self.a1,self.b1,self.c1)
            print("this is instance method from inner class")
s1=sample()
s1.display()
i1=s1.inner1(111,222,333)
print(i1.a,i1.b,i1.c)
i1.display()
i1.display2()
i1.display3()
'''
#we can see data of inner class:
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is class method")
    class inner1:
        a,b,c=10,20,30
        def __init__(self,a1,b1,c1):
            self.a1,self.b1,self.c1=a1,b1,c1
        @classmethod
        def display(cls):
            print(sample.x,sample.y,sample.z)
            print(cls.a,cls.b,cls.c)
            print("this is class method from innner")
        @staticmethod
        def display2():
            print(sample.x,sample.y,sample.z)
            print(sample.inner1.a,sample.inner1.b,sample.inner1.c,)
            print("this is static emthod from inner class")
        def display3(self):
            print(sample.x,sample.y,sample.z)
            print(self.a,self.b,self.c)
            print(self.a1,self.b1,self.c1)
            print("this is instance method from inner class")
print(sample.inner1.a)
print(sample.inner1.b)
print(sample.inner1.c)
'''
#we can see method of inner class:
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is class method")
    class inner1:
        a,b,c=10,20,30
        def __init__(self,a1,b1,c1):
            self.a1,self.b1,self.c1=a1,b1,c1
        @classmethod
        def display(cls):
            print(sample.x,sample.y,sample.z)
            print(cls.a,cls.b,cls.c)
            print("this is class method from innner")
        @staticmethod
        def display2():
            print(sample.x,sample.y,sample.z)
            print(sample.inner1.a,sample.inner1.b,sample.inner1.c,)
            print("this is static emthod from inner class")
        def display3(self):
            print(sample.x,sample.y,sample.z)
            print(self.a,self.b,self.c)
            print(self.a1,self.b1,self.c1)
            print("this is instance method from inner class")
sample.inner1.display()
sample.inner1.diaplay2()
'''
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is class method")
    class inner1:
        a,b,c=10,20,30
        def __init__(self,a1,b1,c1):
            self.a1,self.b1,self.c1=a1,b1,c1
        @classmethod
        def display(cls):
            print(cls.a,cls.b,cls.c)
            print("this is class method from innner")
        @staticmethod
        def display2():
            print("this is static emthod from inner class")
        def display3(self):
            print(self.a,self.b,self.c)
            print(self.a1,self.b1,self.c1)
            print("this is instance method from inner class")
    i1=inner1(111,222,333)
    i1.display()
    i1.display2()
    i1.display3()
'''
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is class method")
    class inner1:
        a,b,c=10,20,30
        def __init__(self,a1,b1,c1):
            self.a1,self.b1,self.c1=a1,b1,c1
        @classmethod
        def display(cls):
            print(cls.a,cls.b,cls.c)
            print(sample().x,sample().y,sample.z)
            print("this is class method from innner")
        @staticmethod
        def display2():
            print(sample().x,sample().y,sample().z)
            print("this is static emthod from inner class")
        def display3(self):
            print(self.a,self.b,self.c)
            print(self.a1,self.b1,self.c1)
            print(sample().x,sample().y,sample().z)
            print("this is instance method from inner class")
sample.inner1.display()
sample.inner1.display2()
sample.inner1(111,222,333).display3()
'''
class sample:
    x,y,z=1,2,3
    def display(self):
        print("this is display method")
print(sample().x,sample().y,sample().z)
sample().display()