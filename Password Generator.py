import random
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","W","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Numbers  = ["1","2","3","4","5","6","7","8","9","0"]
Symbols  = ["!","@","#","&","*","(",")","+"]

print("Welcome to the Password Generator!")

Input_Alphabet = (int(input("How many letters would you like to have in your Password?\n")))
Input_Number   = (int(input("How many numbers would you like?\n")))
Input_Symbol   = (int(input("How many symbols would you like?\n")))

# Easy Version
'''password=" "
for char in range(1,Input_Alphabet):
    password = password + random.choice(Alphabet)
for char in range(1,Input_Number):
    password = password + random.choice(Numbers)
for char in range(1,Input_Symbol):
    password = password + random.choice(Symbols)
print(password)'''

#Hard Version

password_list = []
for char in range(1,Input_Alphabet):
    password_list.append(random.choice(Alphabet))
for char in range(1,Input_Number):
    password_list.append(random.choice(Numbers))
for char in range(1,Input_Symbol):
    password_list.append(random.choice(Symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(password)