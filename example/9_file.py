# Open the txt file
## Read - "r" (default)
f = open(r"example/data1.txt","r")

#print the data in terminal
print(f.read())

## Append - "a" (append text in the end of data)
## Write - "w" (overwrite any existing content)
f = open(r"example/data1.txt","a")

# add text at the and of the line
f.write("Need more Data!")

# add multiple text with enter
f.writelines(["\nNeed more data", "\nmore and more"])

f.close()