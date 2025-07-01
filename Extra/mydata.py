import yaml

# Your Python dictionary
data = {
    'name': 'Sikander',
    'role': 'QA Automation',
    'skills': ['Python', 'Robot Framework', 'Docker']
}

# Write to a YAML file
with open('output.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

print("YAML file created successfully!")