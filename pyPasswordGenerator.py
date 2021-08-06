# //Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
list=[]
len1=len(letters)
len2=len(numbers)
len3=len(symbols)
for i in range(nr_letters):
  l=random.randint(0,len1-1)
  list.append(letters[l])
for i in range(nr_symbols):
  s=random.randint(0,len3-1)
  list.append(symbols[s])
for i in range(nr_numbers):
  n=random.randint(0,len2-1)
  list.append(numbers[n])
s=""
for i in range(len(list)):
  w=random.randint(0,len(list)-1)
  s+=list[w]
print(f"the password is {s}")