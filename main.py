resources = {}

while True:
    item = input().lower().split()
    
    if item[0] == 'total': 
        break

    key = item[0]
    value = item[1]
    
    if key in resources:
        resources[key] += int(value)
    else:
        resources[key] = int(value)
        
for element in sorted(resources):
    print(element, resources[element])
    
    
    
