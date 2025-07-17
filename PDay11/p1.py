name ="aaaa"
d={}
for char in name:
 if char in d:
   d[char] +=1
 else:
   d[char]=1


print(d)