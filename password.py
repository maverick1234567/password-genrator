import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = int(input("enter how many letter you want to enter:"))
nr_numbers = int(input("enter how many number you want to enter:"))
nr_symbols = int(input("enter how many symbol you want to enter:"))

password= ""

for char in range(1, nr_letters + 1):
    password= password + random.choice(letters).lower()
for char in range(1, nr_numbers + 1):
    password= password + random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password= password + random.choice(symbols).lower()

print(password)
