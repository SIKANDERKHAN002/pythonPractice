# def greet():        #Function Declaration
#      print("Hello")
#      print("Hello")
#      print("Hello")
#      print("Hello")
#      print("Hello")
#      print("Hello")

# greet();            #Function calling
# def greet(name):        #Function Declaration
#      """This is print """
#      print(f"THis is name {name}")
#      print(f"THis is name {name}")
#      print(f"THis is name {name}")
#      print(f"THis is name {name}")
#      print(f"THis is name {name}")
#      print(f"THis is name {name}")

# greet("Sikander");            #Function calling


#Function with no arguments and no return typ

# def my_fun():
#     print("Hello")
# print(my_fun())    




#Function with arguments and no retrun type

# def myfun(name):
#     print(f"Hello  {name}")
# myfun("Json")    
# print(myfun("Uber"))    


# #With arguments and with value
# def add(a,b):
#     return a+b
# add(20,30)
# print(add(10,20))


# #No arguments and with return values
# def func():
#     return 10
# print(func())

# def multiple():
#     return 10,20,30
# print(multiple())


#factorial using recurssion
n= input("Enter factorial number")
def fact(n):
    return 5 if n==0 else n*fact(n-1)

print(fact(5))