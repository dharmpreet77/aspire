Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print("Hello admin")
Hello admin
>>> x=20
>>> y=15
>>> z=x+y
>>> print("total sum",z)
total sum 35
>>> x=20
>>> y=10
>>> z=x+y
>>> a=x-y
>>> b=x*y
>>> c=x**y
>>> d=x%y
>>> e=x/y
>>> print("total sum:",z "subtraction",a "multipliction :",b "Exponentiation",c "Modulus : ",d "devide :",e)
SyntaxError: invalid syntax
>>> print("total sum:",z "subtraction",a ,"multipliction :",b ,"Exponentiation",c ,"Modulus : ",d ,"devide :",e)
SyntaxError: invalid syntax
>>> print("total sum:",z ,"subtraction",a ,"multipliction :",b ,"Exponentiation",c, "Modulus : ",d, "devide :",e)
total sum: 30 subtraction 10 multipliction : 200 Exponentiation 10240000000000 Modulus :  0 devide : 2.0
>>> x=int(input("enter the number :"))
enter the number :333
>>> print(x)
333
>>> x=2
>>> y=4
>>> z=x**y
>>> print(z)
16
>>> a=3.14*4**2
>>> print("area of circle",a)
area of circle 50.24
>>> #A= pie r2
>>> a=int(input("square :"))
square :
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a=int(input("square :"))
ValueError: invalid literal for int() with base 10: ''
>>> a=int(input("square"))
square2
>>> b=a*a
>>> print("area of square is",b)
area of square is 4
>>> c=b*b
>>> print(c)
16
>>> width=(input("enter the width of rectangle"))
enter the width of rectangle200
>>> height=(input("enter the height of rectangle"))
enter the height of rectangle200
>>> area=width*height
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    area=width*height
TypeError: can't multiply sequence by non-int of type 'str'
>>> width=int(input("enter the width of rectangle"))
enter the width of rectangle200
>>> height=int(input("enter the height of rectangle"))
enter the height of rectangle150
>>> area=width*height
>>> print("area of rectangle",area)
area of rectangle 30000
>>> 

