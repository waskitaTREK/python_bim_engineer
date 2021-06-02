# List type based on data
list_string = ["Hello","Waskita","!"]
list_boolean = [True,False,True]
list_number = [1,2,3]

list_mix = ["Ryan",25,True,180,"male"]

# state the type of things
print(type(list_string))

# Access List Items
print(list_string[1:])

# Change Item Value's using index number
list_mix[2] = False
##  Insert Item Value based on specific index
list_mix.insert(5,"Jakarta")
## Insert item at the end of the list
list_mix.append("August 15th, 1995")

print(list_mix)

## Append list 1 to list 2
list1 = ["apple", "banana", "cherry", "orange"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)

#Remove item from list
## Remove item from list using item 
list1.remove("banana")

## Remove item using index
list2.pop(0)

## Clear list content
list1.clear()
print(list1)