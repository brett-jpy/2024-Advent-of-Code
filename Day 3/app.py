import re

with open("input.txt", "r") as f:
    data = f.read()

    # A sample regular expression to find digits.  
    regex = r'mul\((\d{1,},\d{1,})\)'             
        
    match = re.findall(regex, str(data))  
    
    data = []
    product = 0
    for m in match:
        new = m.split(",")
        # data.append(( int(new[0]), int(new[1]) ))
        product += (int(new[0]) * int(new[1]))
    
    print(product) # Confirmed Right Answer: 153469856