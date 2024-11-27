import random

print("I will think of a random number and you have to guses it from number 1 to 20")
number=random.randint(1,20)
while True:
    i=int(input("enter your guessed number:--"))
    if number==i:
        print("you have guessed it right")
        print("the number you guessed is",number)
        break
    else:
        print("try another number")