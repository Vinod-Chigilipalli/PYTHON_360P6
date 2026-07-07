'''
print(dir(object))
class sample:
    pass
print(dir(sample))
'''
#example:-1
'''
class sample:
    #class data
    a=10
    b=20
    c=30
class sample2(sample):
    #class data
    x,y,z=1,2,3
print(sample2.a,sample2.b,sample2.c)
print(sample2.x,sample2.y,sample2.z)
'''
#exmaple:-2
'''
class sample:
    a,b,c=11,12,13
    def display(self):
        print("this is from sample!")
class sample2(sample):
    x,y,z=10,20,30
    def display2(self):
        print("this is from sample2!")
s1=sample()
s1.a,s1.b,s1.c=100,200,300
s2=sample2()
s2.display()
s2.display2()
s2.a,s2.b,s2.c=101,201,301
print(s2.a,s2.b,s2.c)
print(sample.a,sample.b,sample.c)
sample.a,sample.b,sample.c=111,222,333
print(s2.a,s2.b,s2.c)
print(sample.a,sample.b,sample.c)
print(s1.a,s1.b,s1.c)
'''
#example:-multiple inheritance
'''
class sample:
    x,y,z=1,2,3
class sample2:
    a,b,c=10,20,30
class sample3(sample,sample2):
    a1,b1,c1=10,20,30
s3=sample3()
print(s3.x,s3.y,s3.z,s3.a,s3.b,s3.c)
print(s3.a1,s3.b1,s3.c1)
'''
#example:-multi-level inheritance
'''
class sample:
    x,y,z=1,2,3
class sample2(sample): #sample2+sample
    a,b,c=10,20,30
class sample3(sample2): #sample3+sample2+sample
    a1,b1,c1=10,20,30
s3=sample3()
print(s3.x,s3.y,s3.z,s3.a,s3.b,s3.c)
print(s3.a1,s3.b1,s3.c1)
'''
'''
class sample:
    a,b,c=10,20,30
class sample2:
    x,y,z=1,2,3
class sample3:
    a,b,c=100,200,300
class sample4(sample,sample2,sample3):
    a1,x1,p,q,r=11,12,13,14,15
s4=sample4()
print(s4.a,s4.x)
print(sample4.__mro__)  #return tuple format
print(sample4.mro()) #return list format
'''
#example:-mro method
'''
class sample:
    a,b,c=10,20,30
class sample2:
    x,y,z,a,b,c=1,2,3,12,13,14
class sample3:
    a,b,c,x,y,z=100,200,300,1,2,3
class sample4(sample,sample2,sample3):
    a1,x1,p,q,r=11,12,13,14,15
s4=sample4()
print(s4.a,s4.b,s4.c,s4.a1,s4.x1)
'''
class sample:
    a,b,c=10,20,30
class sample2:
    x,y,z,a,b,c=1,2,3,12,13,14
class sample3:
    a,b,c,x,y,z=100,200,300,1,2,3
class sample4(sample3,sample2,sample):
    a,b,c=11,12,13
    def display(self):
        print(super().a,super().b,super().c) #super() function to differentiate the super class and sub class
        print(self.a,self.b,self.c)
s4=sample4()
s4.display()