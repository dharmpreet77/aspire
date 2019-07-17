
qu="hello"
print(qu*3)

a="welcome 'Dharm' "
print(a)

b='welcome "Dharm" '
print(b)

c="welcome \\to \tour \ninternet cafe"
print("tab space and new line = ",c)

d="welcome Admin" #arry
print(d[9])

#length count

x="gateway"
print("word length =",len(x))

#counting substrings in a string
pk="gateway solutions"
p=pk.count("solutions")
print("count = ",p)
#slicing
e="gateway solutions"
print(e[8:])
print(e[2:7])
print(e[0:7])

#search character in string
print("c" in d,"q" in d)

    
#string plus #concatenation

name="hello"+"preet"
print(name)

nm="hello"+ " " + "preet"
print(nm)



#convert integer vakue to string
age=21
nm1="Arsh"+ " " + str(age)
print(nm1)



#INDEXING ON STRING

aa="dharmpreet"
n=len(aa)
i=0
while i<n:
    print(aa[i])
    i+=1
#access each letter
for i in aa:print(i,end=' ')
#reverse order
for i in aa[:: -1]:
    print(i,end=' ')



#list
list=["red","green","blue","yellow","pink"]
print(list)
list.insert(0,"brown")      #insert item
list[2]="black"              #replace item
list.remove("blue")         #remove item
print("list of color",list)



#remove space from a string

jj=" Arshpreet singh "
print(jj)
print(jj.lstrip())  #remove space at left
print(jj.rstrip())  #remove space at right
print(jj.strip())   #remove space from both sides








