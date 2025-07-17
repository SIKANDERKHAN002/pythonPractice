#factorial using recurssion
# n= input("Enter factorial number")
# def fact(n):
#     return 5 if n==0 else n*fact(n-1)

# print(fact(5))


import random
import string


def  generate_password(length):
    chars = string.ascii_letters + string.digits + '@#$%&*!'
    print(random.choice(chars))
    s=""
    for i in range(length):
        s+=s.join(random.choice(chars))
    return s

print(generate_password(10))   