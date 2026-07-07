'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    data=1
    for colnum in range(1,rownum+1):
        print(data,end=" ")
        data+=1
    print()
'''

'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    for colnum in range(1,rownum+1):
        print(rownum,end=" ")
    print()
'''
'''
rows=int(input("rows:"))
cpr=rows
for rownum in range(1,rows+1):
    data=1
    for colnum in range(1,cpr+1):
        print(data,end=" ")
        data+=1
    print()
    cpr-=1
'''
'''
rows=int(input("rows:"))
cpr=rows
for rownum in range(1,rows+1):
    data=5
    for colnum in range(1,cpr+1):
        print(data,end=" ")
        data-=1
    print()
    cpr-=1
'''
'''
rows=int(input("rows:"))
data=1
for rownum in range(1,rows+1):
    for colnum in range(1,rownum+1):
        print(data,end=" ")
        data+=2
    print()
'''
'''
rows=int(input("rows:"))
cpr=rows
for rownum in range(1,rows+1):
    for colnum in range(1,cpr+1):
        print("*",end="")
    print()
    cpr-=1       
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    data=1
    print(" " *(rows-rownum+1),end=" ")
    for colnum in range(1,rownum+1):
        print(data,end=" ")
        data+=1
    print()
'''

'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    for colnum in range(1,rownum+1):
        if colnum==rownum:
            print(rownum,end="")
        else:
            print(0,end="")
    print()
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    print(" "*(rows-rownum+1),"* "*(rownum))
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    print(" "*(rownum),"* "*(rows-rownum+1))
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    print(" "*(rows-rownum+1),*range(1,rownum+1),*range(rownum-1,0,-1))
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    if rownum%2==0:
        print("01"*((rows+1)//2))
    else:
        print("10"*((rows+1)//2))
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    for colnum in range(1,rownum+1):
        if colnum%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    print(" "*(rownum),rownum,sep="")
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    print(" "*(rows-rownum+1),rownum,sep="")
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    data=65
    for colnum in range(1,(rows-rownum+1)+1):
        print(chr(data),end=" ")
        data+=1
    print()
'''
'''
rows=int(input("rows:"))
for rownum in range(1,rows+1):
    data=65+rownum-1
    for colnum in range(1,(rows-rownum+1)+1):
        print(chr(data),end=" ")
        data+=1
    print()
'''
'''
number=int(input("Enter the number:"))
sum=0
while number!=0:
    sum+=number%10
    number//=10
print(sum)
'''