from itertools import tee, islice, zip_longest

working_data = []

# Read File line by line
with open("values.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
    for l in lines:
        working_data.append(l.rstrip().split(" ")) # rstrip - removes the white space characters besides space (i.e., \r , \t , \n)

# Generate Pairs
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

output = []

# Add pairs to tmp list and then add list to parent
for wd in working_data:
    tmp = []
    z = pairwise(wd)
    for i in z:
        tmp.append(i)
    output.append(tmp)

counter = 0
for o in output:
    # Find the length of the list of pairs
    l = len(o)
    # Print for santity - e.g., [('26', '25'), ('25', '24'), ('24', '22'), ('22', '21'), ('21', '19')]
    print("Length: ", l, "List: ", o)
    # Temporary list
    tmp = []

    for item in o:
        # print the sub item - e.g., ('26', '25')
        print(item)
        # Check if the first number is larger than the second
        if int(item[0]) > int(item[1]):
            # subtract the second from the first
            ans = int(item[0]) - int(item[1])
            # If answer is less than or equal 3 and greater tahn or equal 1
            if ans <= 3 and ans >= 1:
                # Add "Up" to temporary list
                tmp.append("Up")
                print("Up")
        # Do the opposite of the above
        elif int(item[0]) < int(item[1]):
            ans = int(item[1]) - int(item[0])
            if ans <= 3 and ans >= 1:
                tmp.append("Down")
                print("Down")
    # Sanity check
    print(tmp)
    print("------------\n")
    # Check if the length of the temporary list equals the length of the original
    if len(tmp) == l:
        # Count the occurances of "Up" or "Down"
        ct_true = tmp.count("Up")
        ct_false = tmp.count("Down")
        # Check if count is equal to length - this is because in order to be "safe" the list must only increment or decrement
        if len(tmp) == ct_true:
            counter += 1
        elif len(tmp) == ct_false:
            counter += 1

print(counter) # 670 - verified correct