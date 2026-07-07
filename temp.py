'''
#write a python program to print swapping two numbers using third variable:
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
temp=a
a=b
b=temp
print("a:",a,"b:",b)
'''
'''
s1=float(input("s1:"))
s2=float(input("s2:"))
s3=float(input("s3:"))
s4=float(input("s4:"))
s5=float(input("s5:"))
if s1<35 or s2>65 or s3<=35 or s4>94 or s5>90:
    print("Result=fail")
else:
    total=s1+s2+s3+s4+s5
    print("Total marks:",total)
    avg=total//5
    print("Average marks:",avg)
    print("result=pass")
    if avg>90:
        print("O grade")
    elif (avg>=80 and avg<=79):
        print("A grade")
    elif (avg>=50 and avg<=69):
        prin
'''
'''
salary=float(input("Enter a salary:"))
if salary>=25000:
    tax=salary*0.13
    print("Tax amount:",tax)
    salary=salary-tax
    print("Remaining salary:",salary)
else:
    print("No tax")
'''
'''
import cmath
print("Enter equation values")
a=float(input("A:"))
b=float(input("B:"))
c=float(input("C:"))
d=(b**2)-(4*a*c)
print("D value:",d)
if d==0:
    print("Roots are real and equal")
    root1=b//(2*a)
    root2=b//(2*a)
    print("Root1:",root1)
    print("Root2:",root2)
elif d>0:
    print("Roots are real and diff")
    root1=-b+cmath.sqrt(d)/(2*a)
    root2=-b-cmath.sqrt(d)/(2*a)
    print("Root1:",root1)
    print("Root2:",root2)
else:
    print("Roots are imagnary")
'''
#write a python program to check given number is prime or not:
'''
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("Not a prime number")
'''
#write a python program to print prime nmbersbetween minimum to maximum:
'''
min=int(input("Enter min number:"))
max=int(input("Enter max number:"))
for num in range(min,max+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)
'''
#write a python program to check the given number is perfect or not:
'''
num=int(input("Enter the number:"))
sum=0
for i in range(1,num//2+1):
    if (num%i==0):
        sum+=i
if (sum==num):
    print("perfect number")
else:
    print("Not perfect number")
'''
#write a python program to print perfect numbers between minimum and maximum:
'''
min=int(input("Enter min number:"))
max=int(input("Enter max number:"))
for num in range(min,max+1):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num)
'''