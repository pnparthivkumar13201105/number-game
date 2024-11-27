import math
print("the ceil of 3.14 is "+ str(math.ceil(3.14)))
print("\nthe floor of 3.14 is "+ str(math.floor(3.14)))

print("\nenter two number to find thier HCF\n")
num1=int(input("enter the first number:---\n"))
num2=int(input("enter te second number:---\n"))
print("the HCF of ",num1,"and",num2,"is"+ str(math.gcd(num1,num2)))