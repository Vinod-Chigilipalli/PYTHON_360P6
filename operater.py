'''
#1.write a python program to find the remainder of the give two numbers without using "%".
a=int(input("a:"))
b=int(input("b:"))
print(a) if a<b else print(a-(b)*(a//b))
'''
'''
#2.write a python to check given number is even or odd without using relational operator.
a=int(input("a:"))
print("odd") if a%2 else print("even")
'''
'''
#3.write a python program find the addition of the two numbers without using "+".
a=int(input("a:"))
b=int(input("b:"))
print(a-(-b))
'''
'''
#4.write a python program to remove the duplicate element from the give list.
l=[1,2,3,3,2,1,4]
print([*{*l}])
'''
'''
#5.print the even number for the given range:
start=int(input("start:"))
end=int(input("end:"))
start=start+1 if start%2 else start
print([*range(start,end,2)])
'''
'''
#6.write a python program to count the number of even number in the given range:
start=int(input("start:"))
end=int(input("end:"))
start=start+1 if start%2 else start
end=end-1 if end%2 else end
print("count:",((end-start)//2)+1)
'''
#7.write a python program to check the given number contains prime digits or not.
n=int(input("n:"))
print("yes") if '2' in f'{n}' or '3' in f'{n}' or '5' in f'{n}' or '7' in f'{n}' else print("no")