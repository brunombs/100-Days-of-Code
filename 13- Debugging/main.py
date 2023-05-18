############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# Awnser:
# The bug with this def is the for loop, it will run between 1 and 19, so it will never print the message.
# In order to that happen, it's necessary to add at least 1 number to the second parameter.

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Awnser:
# This bug is similar to the previous one, it happens when the dice_num is 6 because it means that the
# program will look for a index[6] and there's none, the index is from 0 to 5.

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Awnser:
# The problem with this is that when the user input the number of 1994 it will generate no awnser.
# So to fix this, it's necessary to use <= or >= in the code. Or change "year > 1994" for "year > 1993

# Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

# Awnser:
# One problem with the code above is the missing indentation in the print line.
# Other problem with this code is that input=str, we have to change it to int.

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Awnser:
# The problem with the code above is the "==" in the var "word_per_page" which should be "=".

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# Awnser:

# In this last code the problem is with the b_list.append, it out of the correct indentation block.