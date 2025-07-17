# s=    "Sikander"
# ch2= 'Sikanderkhan'
# ch3= """This is my 
#        bad 
#        good"""

# print(s)
# print(ch2)
# print(ch3)

# print(f"This is my name {ch2}")

# print(s[0])
#<---------------------------------------------------------------------------------------------------------->
# print(len(s))
# print(s[0:10])
# print(s[0:8:-1])
# print(s[8:0:-1])

# ch3= '''This is my 
#        bad 
#        good'''
# print(ch3)

# print("Hello how \"are\" you")
# print(s[13])

# print(s[-2:8:-1])

# 0  1  2  3  4  5      6    7
# s  i  k  a  n     d      e    r
#             -4   -3  -2   -1
# print("a"+10)
# print("10"*"dell")

# sp="Sikander"
# print("r" in sp)
# print("z" not in sp)
# print(ord("a"))
# print(ord("A"))
# print(chr(98))
# print(chr(99))
# print(chr(100))
# print(chr(101))
# print(chr(102))

# a="Dell"
# b="Bell"
# print(a>b)
# print(a<b)

#########################Question1
# spl= "-dell-"
# print(spl.strip("-"))
# print(spl.lstrip("-")) 
# print(spl.rstrip("-"))  


# subStr="This is good"
# print(subStr.find("oo"))
# try:
#    print(subStr.index("oop"))
# except  Exception as e :
#    print(f"This is error =====> {e}")
# finally:
#    print("index testing closed")   
      

# rstring="thisis lefteeee"
# print(rstring.rfind('o'))      
# print(rstring.rindex('t'))    
# print(rstring)  
# print(rstring.count('e'))
# print(rstring.replace("le","--new--"))
# print(rstring)

# leftv="sika nder"
# vtag= leftv.split()
# print(type(vtag))
# print(vtag)
# print(vtag[0])
# for i in vtag:
#    print(i)
# result="manfore"
# for i in result:
#    print(i)   


# word = "manage"
# result = word.split()
# print("Split without delimiter:", result)


# a="aaaa"
# b="bbbb"

# print(a.join(b))


# s="learning python is very easy"
# print(s.startswith("learnin"))
# print(s.endswith("easy"))


s="asdf sdfad"
# s2="this is stringss"
# print(s.upper())
# l="LOWER"
# print(l.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#Query
# print(s.casefold())
# print(s.casefold() == s2.casefold())

print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())
print(s.isalpha())