import re

with open("input.txt", "r") as f:
    data = f.read()

    # A sample regular expression to find digits.  
    regex = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'             
        
    match = re.findall(regex, str(data))  
        
    # Assume that all anything without a do/don't is valid (like the first example)
    output = 0
    check = True
    for item in match:
        if item == "do()":
            check = True
        elif item == "don\'t()":
            check = False
        elif check:
            nums = re.findall(r'\d{1,3}', item)
            output += int(nums[0]) * int(nums[1])

print(output) # 77055967 Confirmed Right Answer