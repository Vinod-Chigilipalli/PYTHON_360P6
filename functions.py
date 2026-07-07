'''
#factorial using recursive function:
def factorial(n):
    if n==0: #Base case
        return 1
    else: #Recursive case
        return n*factorial(n-1)
print(factorial(4))
'''
'''
#print numbers 1 to n:
def print_number(n):
    if n==0: #base case
        return 1
    print_number(n-1) #recursive case
    print(n)
print_number(10)
'''
'''
#sum of first n numbers:
def sum_numbers(n):
    if n==0:
        return 1
    else:
        return n+sum_numbers(n-1)
print(sum_numbers(8))
'''
'''
#write a python program to find the number of vowels in the given string using recursive:
string=input("string:")
length=0
for _ in string:
    length+=1
def count_vowels(index,length,count):
    if index<length:
        if string[index] in "aeiouAEIOU":
            count_vowels(index+1,length,count+1)
        else:
            count_vowels(index+1,length,count)
    else:
        print(count)
count_vowels(0,length,0)
'''
'''
#reverse the given string using recursive without slicing:
string=input("string:")
length=0
for _ in string:
    length+=1
def reverse(index):
    if index>=0:
        print(string[index],end="")
        reverse(index-1)
reverse(length-1)
'''
'''
#loop and with using rercursion,not allowed to use range():
rows=int(input("rows:"))
def row(colnum,data,rownum):
    if colnum<=rownum:
        print(data,end=" ")
        row(colnum+1,data+1,rownum)
def pattern(rownum,rows):
    if rownum<=rows:
        row(1,1,rownum)
        print()
'''
#monkey patching:
'''
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
add(2,4)
add=sub
sub(2,4)
mul=add
mul(2,4)
'''
#decorator function:
'''
def decorator1(func):
    def wrapper():
        func()
        print("This is from decorator1")
    return wrapper
def decorator2(func):
    def wrapper():
        func()
        print("This is from decorator2")
    return wrapper
@decorator2
@decorator1
def dec_wrapper():
    print("This is from dec_wrapper")
dec_wrapper()
'''
#exapmle:-1
'''
def add_sprinkless(func):
    def wrapper(*args,**keyargs):
        func(*args,**keyargs)
        print("*You add sprinkless*")
    return wrapper
def add_fundge(func):
    def wrapper(*args,**keyargs):
        func(*args,**keyargs)
        print("*You add fundge*")
    return wrapper
@add_fundge
@add_sprinkless
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")
get_ice_cream("chocolate")
'''
#exapmle:-2
'''
def minor(func):
    def wrapper():
        amt=func()
        print("Minor interest ammount:",amt*0.3/100)
        return amt
    return wrapper
def major(func):
    def wrapper():
        amt=func()
        print("Major intererst amount:",amt*0.3/100)
        return amt
    return wrapper
@major
@minor
def interest_amount():
    amount=int(input("Enter the amount:"))
    return amount
interest_amount()
'''
#generator function:
#example:-1
'''
def display():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
g=display()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
#example:-2
'''
def display():
    yield 1
    yield 2
    yield 3
    yield 4
g1=display()
print([*g1])
'''
#example:-3
'''
def display():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
g1=display()
for i in g1:
    print(i)
'''
#example:-4
'''
g1=(i for i in range(1,11))
print(type(g1))
print(*g1)
g1=(i for i in range(1,11) if i>=5)
print(type(g1))
print(*g1)
'''
#example:-5
'''
g1=(i for i in "abcdef" if i not in "aeiouAEIOU")
print(*g1,sep="")
'''
s1=input("Enter the string:")
def words():
    word=""
    for i in s1:
        if i!=" ":
            word+=i
        else:
            if word!="":
                yield word
            word=''
    yield word
g1=words()
for i in g1:
    print(i)