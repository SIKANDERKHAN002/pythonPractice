#Nested For loop
envTypes=["Dev","Testing","Production"]
features=["login","search","addToCart"]

for item in envTypes:
    for  feature in features:
        print(f"{item} and {feature}")

n=5
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")        
    print()    


