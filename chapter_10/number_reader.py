import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)
