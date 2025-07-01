import yaml

with open("readFile.yaml","r") as f:
    data = yaml.safe_load(f)

print(data)
print(data["key"])
print(data["mylist"][0])
print(data["mylist"][1])
print(data["mylist"][2])
print(data["multi-line-str"])