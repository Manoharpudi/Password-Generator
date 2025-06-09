import random
import string

def gen_password(length):
    character=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(character) for i in range(length))
    return password

try:
    len=int(input("Enter the desired password length: "))
    if len<=0:
        print("Password length should be greater than 0")
    else:
        gen_password=gen_password(len)

        print("Your generated password is ", gen_password)

except ValueError:
    print("Enter Numeric value for length to generate password")


    