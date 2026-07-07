'''
#write a python program to find who is the highest score and person name in the given dictionary.
d1={'sachin':140,'kohli':150,'rohit':100,'smith':50}
maximum=d1['kohli']
name=""
for key in d1:
    if maximum<d1[key]:
        maximum=d1[key]
        name=key
print(name,maximum)
'''
'''find the frequency of the given string using dictionary,
where we need to print the given string each character as key and 
its frequency as a value in the dictionary result:

s1=input("string")
d1={}
for i in s1:
    d1[i]=0
print(d1)
for i in d1:
    count=0
    for j in s1:
        if i==j:
            count+=1
    d1[i]=count
print(d1)
'''
'''
#write a python program to rremove the given string from the whole string,print the result as string:
s1=input("original string")
s2=input("string")
len1=len2=0
for i in s1:
    len1+=1
for i in s2:
    len2+=1
result=""
index=0
while index<len1:
    if s1[index:index+len2]==s2:
        index+=len2
    else:
        result+=s1[index]
        index+=1
print(result)
'''
'''
s1=input("original string")
s2=input("string")
len1=len2=1
result=""
index=0
count=0
while index<len1:
    if s1[index:index+len2]==s2:
        print("its is present")
        count+=1
        break
    index+=1
if count==0:
    print("not present")
'''