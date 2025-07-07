import keyword

# 1. Types of Data ==>Done
# 2. While loop ==> even odd > 
# 3. Conditions if else elif/ continue / break / pass
# 4. All keyowrds ==>Done
# listDataType=  [int,float,bool,str,set,frozenset,list,tuple,range,dict,complex,None,bytes,bytearray]
# print(listDataType)
# print("------------------------------------------listDataType-----------------------------------------------")
# length=  len(listDataType)-1
# print(length)
# print("----------------------------------------listDataType length------------------------------------------")
# while length>=0:
#       print(f"Data type {length} {listDataType[length]}")
#       length-=1

# TotalkeywordsInPython = ["True","False","None","and","as","await","continue","break","Pass","assert","def","del","if","elif","else","while","for","except","finally","global","import","in","is","lambda","nonlocal","not","not","or","pass","raise","return","try","while","with","yield"]
# print(len(TotalkeywordsInPython))
# print(len(keyword.kwlist))
# print(keyword.kwlist)


# number= int(input("Enter Number \t "))
# print(type(number))
# n=1
# while number!=None:
#       if number%2==0:
#             print("Even number")
#       else:
#             print("Odd Number")
#       n+=1
#       break

# s="sikander"
# del s[0]
# del s
# print(s)

# print("Hello\rWorld\ree123456")
a,b=10,20

# temp=a
# a=b
# b=temp
# print(f"value of a {a} and value of b {b}")

a,b=10,50

a=a+b
b=a-b
a=a-b
print(a,b)

c,d=90,100
d,c=c,d

print(c)
print(d)
