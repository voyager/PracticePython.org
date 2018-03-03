"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

name = input("Enter your name: ")
age = input("Enter your age: ")

# diff = 100 - int(age)

# print(name + ", in " + str(diff) + " years you will be 100 years old!")

for i in range(int(input("How many times do you want to see this: "))):
  print(name + ", in " + str(100 - int(age)) + " years you will be 100 years old!\n")
