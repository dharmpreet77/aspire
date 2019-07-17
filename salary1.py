salary=int(input("salary = "))
a=int(salary)
hra=a*14/100
print("HRA 14% : ",hra)
com=a*6/100
print("COM 6% : ",com)
ta=a*5/100
print("TA 5% : ",ta)
ea=a*14/100
print("EA 14% : ",ea)
da=a*10/100
print("DA 10% : ",da)
sum=hra+com+ta+ea+da+a
print("Total Gross Salary",sum)

tax=int(sum*5)/100
print("Tax 5% : ",tax)
ns=sum-tax
print("Total Net Value : ",ns)
