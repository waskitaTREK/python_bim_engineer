# Open the txt file
## Read - "r" (default)
f = open("D:\WASKITA2\python_bim_engineer\example\data1.txt","r")

#print the data in terminal
print(f.read())

## Append - "a" (append text in the end of data)
## Write - "w" (overwrite any existing content)
f = open("D:\WASKITA2\python_bim_engineer\example\data1.txt","a")
f.write("Need more Data!")