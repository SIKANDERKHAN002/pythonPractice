import json
import yaml

#Sample Dictionary
employee_01={
    "name": "Martin",
    "job": "Developer",
    "skill": "Elites",
    "employed": True,    
}

print(type(employee_01))
print(employee_01)
#serialization
json_object = json.dumps(employee_01)
print("#################")
print(json_object)
print(type(json_object))
#Writing to a file
with  open('users.yaml','w') as f:
    data = yaml.dump(json_object,f)