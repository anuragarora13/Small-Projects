
import random
from operator import concat

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy Level
# print(random.choice(letters))
# print(random.choice(numbers))
# print(random.choice(symbols))

# length_password=nr_letters+nr_numbers+nr_symbols

# password=random.choices(letters,k=nr_letters))+random.choices(numbers,k=nr_numbers))+random.choices(symbols,k=nr_symbols))


# for i in range(1,(length_password+1)):
#
# password = ''
# for i in range(1,nr_letters+1):
#     password+=random.choice(letters)
#
# for i in range(1, nr_symbols+1):
#     password += random.choice(symbols)
#
# for i in range(1, nr_numbers+1):
#     password += random.choice(numbers)

# print(password)

lists=random.choices(letters,k=nr_letters)+random.choices(symbols,k=nr_symbols)+random.choices(numbers,k=nr_numbers)
random.shuffle(lists)
password=''
for i in lists:
    password+=i
print('your password is:',password)


