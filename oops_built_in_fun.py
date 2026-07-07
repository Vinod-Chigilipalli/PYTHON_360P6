#using "getattr" function:
'''
class sample:
    a,b=10,20
    def __init__(self):
        self.x,self.y=11,12
print(sample.a,sample.b)
print(getattr(sample,"a"))
print(getattr(sample,"b"))
print(getattr(sample,"c","given name is not there"))
print(dir(sample))
'''
'''
class sample:
    a,b=10,20
    def __init__(self):
        self.x,self.y=11,12
s1=sample()
print(sample.a,sample.b)
print(getattr(sample,"a"))
print(getattr(sample,"b"))
print(getattr(sample,"c","given name is not there"))
print(getattr(s1,"x"))
print(getattr(s1,"y"))
print(getattr(s1,"a"))
print(getattr(s1,"b"))
print(getattr(s1,"z","given name is not present"))
'''
#using "setattr" function:
'''
class sample:
    a,b=10,20
    def __init__(self):
        self.x,self.y=11,12
s1=sample()
print(sample.a,sample.b)
setattr(sample,"a",100)
setattr(sample,"b",200)
setattr(sample,"c",300)
print(sample.a,sample.b,sample.c)
print(dir(sample))
'''
'''
class sample:
    a,b=10,20
    def __init__(self):
        self.x,self.y=11,12
s1=sample()
print(sample.a,sample.b)
setattr(s1,"a",100)
setattr(s1,"b",200)
setattr(sample,"c",300)
print(sample.a,sample.b,sample.c)
setattr(s1,"x",110)
setattr(s1,"y",220)
setattr(s1,"z",330)
print(s1.x,s1.y,s1.z)
print(dir(s1))
'''
'''
class sample:
    pass
s1=sample()
setattr(sample,"a",100)
setattr(sample,"b",200)
setattr(sample,"c",300)
print(dir(sample))
setattr(s1,"x",11)
setattr(s1,"y",12)
setattr(s1,"z",13)
print(dir(s1))
'''
#using "delattr" function
'''
class sample:
    a,b,c=10,20,30
    def __init__(self):
        self.x,self.y,self.z=11,12,13
s1=sample()
delattr(sample,"a")
delattr(sample,"b")
delattr(s1,"x")
delattr(s1,"y")
print(dir(s1))
'''