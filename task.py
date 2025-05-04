import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level
password = ""
for i in range(1,nr_letters +1):
    letter = random.choice(letters)             # use the list as an alternative of string. it is use for shuffle().
    # string concatenate
    password =  password + letter
for i in range(0, nr_symbols):
    password =  password +  random.choice(symbols)
for i in range(0, nr_numbers):
    password = password +  random.choice(numbers)

print(f"your's sequenced password is: \n {password}")


#  Hard level
password = []
for i in range(1,nr_letters +1):
    password.append(random.choice(letters))             # use the list as an alternative of string. it is use for shuffle().
for i in range(0, nr_symbols):
    password.append(random.choice(symbols))
for i in range(0, nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
s = ""
for i in password:
    s += i
print(f"Your's final password1 is: \n {s}")


# other way
a = list()
for i in range(0,len(password)):   # convert string to list
    a.append(password[i])
random.shuffle(a)                  # shuffle
# print(a)
final_password = ""
for i in range(0,len(a)):
    final_password += a[i]         # convert list to string
print(f"your's final password2 is:\n{final_password}")


# other way
final_password1= random.sample(password,len(password))
# print(final_password1)
b =""
for i in range(0,len(final_password1)):
    b += final_password1[i]
print(f"your's final password3 is: \n {b}")
