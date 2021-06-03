#Tuple
tuple = ("Hello","Waskita","!")
print(type(tuple))

##Tuple can't be edited, appended, or deleted
#tuple[1] = False
#print(tuple)

#Dictionary
## {key : value}
dict = {
    "name": "Ryan",
    "lastname": "",
    "Age":25,
    "Height":180.5,
    "Gender":"Male"
    }
## To call out the data, write the key of the wanted value
print(dict["name"])

## If we want to change the value, we need to access the key
dict["lastname"] = "Gosling"
## If we want access the values
print(dict.values())
## If we want to access the keys
print(dict.keys())

## You can delete the values by accessing the keys
dict.pop("lastname")
print(dict)

## Nested Dictionary
nestedDict = {
    "participant1" : {
        "name": "Ryan",
        "lastname": "",
        "Age":25,
        "Height":180.5,
        "Gender":"Male"
    },
    "participant2" : {
        "name": "Loco",
        "lastname": "Polo",
        "Age":26,
        "Height":170.9,
        "Gender":"Male"
    }
}
print(nestedDict["participant1"]["name"])