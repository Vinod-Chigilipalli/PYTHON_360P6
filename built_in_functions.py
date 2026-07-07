'''
#write a python program get the all prime numbers from 1 to 100 using higher order function:
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
         if n!=1:
             return True
print(list(filter(prime,range(1,100))))
'''
'''
#write a python program to remove the vowels of the given string,print the result as a string using higher order function:
s1=input("string:")
print(*filter(lambda a:a not in "aeiouAEIOU",s1),sep="")
'''

'''
#print the following pattern using higher order functions:
rows=int(input("rows:"))
for i in map(lambda x:range(1,x+1),range(1,rows+1)):
    print(*i)
'''
'''write python program to validate the given email username and password,
where wrapper fun will take both username is always "abc" and password "1234",
login validation we need to validate using decorator:

def login_validation(login):
    def wrapper():
        username,password=login()
        if username=="abc" and password=="1234":
            print("This email account is login sucessful!")
        else:
            print("This email account is not login sucessful!")
    return wrapper
@login_validation
def account_login():
    username=input("Enter the username:")
    password=input("Enter the password:")
    return username,password
account_login()
'''
'''
start=int(input("start:"))
end=int(input("end:"))
def prime(start,end):
    for n in range(start,end+1):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                yield n
g=prime(start,end)
for x in g:
    print(x)
'''
'''
#find the first non repeating elements using dictionary:
l1=[1,2,3,4,1,2,5,4,3]
d={}
for i in l1:
    d[i]=d.get(i,0)+1
for i in l1:
    if d[i]==1:
        print(i)
        break
'''
#zip():
'''
l1=["vinod","sai","bhasa"]
l2=[22,20,21]
result=zip(l1,l2)
print(*result)
'''