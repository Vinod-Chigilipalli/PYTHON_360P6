'''
class sample:
    #class data
    a,b,c=10,20,30
    #method
    def display(self):
        print("This is my first instance method!")
print(sample.a)
print(sample.b)
print(sample.c)
s1=sample()
s1.display()
'''
'''
class sample:
    a,b,c=10,20,30
    #class method
    @classmethod
    def display1(cls):
        print("This is class method from sample")
    #static method
    @staticmethod
    def display2():
        print("This is static method from sample")
    #instance method
    def display3(self):
        print("This is instance method from sample")
print(sample.a,sample.b,sample.c)
sample.diaplay1
sample.diaplay2
s1=sample()
s1.display3()
'''
'''
class sample:
    """default constructor"""
    def __init__(self):
        print("This is default constructor")
s1=sample()
'''
'''
class sample:
    #parameterized constructor
    def __init__(self,a,b,c):
        print("This is parametrized constructor")
        print(a,b,c)
s1=sample(10,20,30)
'''
'''
#instance method using self.name:
class sample:
    #parameterized constructor
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
s1=sample(10,20,30)
print(s1.a)
print(s1.b)
print(s1.c)
'''
'''
class sample:
    #parametrized constructor
    def __init__(self):
        self.a=int(input("a:"))
        self.b=int(input("b:"))
        self.c=int(input("c:"))
s1=sample()
print(s1.a)
print(s1.b)
print(s1.c)
'''
'''
#class method using cls and static method:
class sample:
    a,b,c=10,20,30  #class data
    @classmethod
    def display1(cls):
        print(cls.a,cls.b,cls.c)
    @staicmethod
    def display2():
        print(sample.a,sample.b,sample.c)
sample.display1()
sample.display2()
'''
'''class sample:
    x,y,z=10,20,30
    def __init__(self):
        self.a1,self.b1,self.c1=100,200,300
    @classmethod
    def display1(cls):
        print("this is class method!")
    @staticmethod
    def display2():
        print("this is static method!")
    def display3(self):
        print(self.x,self.y,self.z)
        print(self.a1,self.b1,self.c1)
        self.display1()
        self.display2()
s1=sample()
s1.display3()
'''
'''
class sample:
    a1,b1,c1=10,20,30
    @classmethod
    def display1(cls):
        cls.a1,cls.b1,cls.c1=100,200,300
    @staticmethod
    def display2():
        sample.a1,sample.b1,sample.c1=1,2,3
print(sample.a1,sample.b1,sample.c1)
sample.display1()
print(sample.a1,sample.b1,sample.c1)
sample.display2()
print(sample.a1,sample.b1,sample.c1)
'''
'''
class sample:
    a1,b1,c1=10,20,30
    def display(self):
        self.a1=100
        self.b1=200
        self.c1=300
print(sample.a1,sample.b1,sample.c1)
s1=sample()
s1.display()
print(s1.a1,s1.b1,s1.c1)
'''
'''
class sample:
    a1,b1,c1=10,20,30
    def __init__(self):
        self.x,self.y,self.z=1,2,3
    def display(self):
        self.a1=101
        self.b1=202
        self.c1=303
        self.x,self.y,self.z=11,22,33
print(sample.a1,sample.b1,sample.c1)
s1=sample()
s1.display()
print(s1.a1,s1.b1,s1.c1)
'''
'''
class sample:
    a1,b1,c1=10,20,30
    def __init__(self):
        self.x,self.y,self.z=1,2,3
print(sample.a1,sample.b1,sample.c1)
sample.a1,sample.b1,sample.c1=11,12,13
print(sample.a1,sample.b1,sample.c1)
s1=sample()
print(s1.x,s1.y,s1.z)
s1.x,s1.y,s1.z=100,200,300
print(s1.x,s1.y,s1.z)
'''
'''
class sample:
    a,b,c=10,20,30
    def __init__(self):
        self.a1,self.b1,self.c1=10,20,40
    @classmethod
    def display1(cls):pass
    @staticmethod
    def display2():pass
    def display3(self):pass
s1=sample()
print(dir(sample))
print(dir(s1))
'''
#when we want to call the class method inside the same class
'''
class sample:
    @classmethod
    def display1(cls):
        print("this class method-display1")
    @classmethod
    def display2(cls):
        cls.display1()
        print("this class method-display2")
    @staticmethod
    def display3():
        sample.display1()
        print("this static method-display3")
    def display4(self):
        self.display1()
        print("this instance method-display4")
s1=sample()
s1.display2()
s1.display3()
s1.display4()
'''
#when we want to call the static method inside the same class
'''
class sample:
    @classmethod
    def display(cls):
        print("this class method-display")
        cls.display2()
        cls.display3()
    @staticmethod
    def display2():
        print("this static method-display2")
    @staticmethod
    def display3():
        sample.display2()
        print("this static method-display3")
    def display4(self):
        self.display2()
        print("this instance method-display4")
s1=sample()
s1.display()
s1.display3()
s1.display4()
'''
#when we want to access the any instance method of the class
class sample:
    def display3(self):
        print("this instance method-display3")
    def display4(self):
        self.display3()
        print("this instance method-dispaly4")
s1=sample()
s1.display4()