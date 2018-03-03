"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras: 

1.  If the number is a multiple of 4, print out a different message.
2.  Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


num = int(input("Enter the first number: "))
check = int(input("and another number: "))

four = num/check % 4

if num % 4 == 0:
  print(str(num) + " is multiple of 4!")
elif num % 2 == 0:
  print(str(num) + " is even, but it's not multiple of 4!")
else:
  print(str(num) + " is odd!")
  
if num % check == 0:
  print(str(num) + " divides evenly by " + str(check))
else:
  print(str(num) + " does not divide evenly by " + str(check))
