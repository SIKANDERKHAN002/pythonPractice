# s= {}
# print(type(s))

# s= {10,10.5,True,"Welcome",True,1}

# print(s)
# p ={10,}
# print(type(p))


# s = eval(input("Enter set:"))
# print(type(s))
# print(s)

# p = set(range(10))
# print(p)

# k= "Learning python is easy"
# k1 = k.split()
# k3 = set(k1)
# print(k3)

# for i in k3:
#     print(i)
s = {10,20,30}
#Functions on set
# print(s)
# s.add(40)
# print(s)

# s.update([90,80,70])
# print(s)

# copyIt = s.copy()
# print(copyIt)

# print(s.pop())
# print(s)
# print(copyIt)

# s.remove(90)
# print(s)


# print(hash(1))
# print(hash(True))

# print(hash(100))
# print(hash(100))

x = [10,20,30,40]
 
y = { i for i in x }
print(y)

lp = [10,[16,17,18],[20,30,40]]
for item in lp:
    if isinstance(item,list):
         for i in item:
              print(i)
    else:
         print(item)