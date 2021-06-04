numbers = [0,1,2,3,4]

person = {"name": "Fahmi", "age": 25, "height":1.65}

try:
    numbers[9] = 9 # will trigger IndexError
    person["weight"] # will trigger KeyError
    a = 2 + 'j' # will trigger other error

except KeyError:
    # do other stuff needed when error happen

    print("this person doesn't have weight")

except IndexError:
    # do other stuff needed when error happen
    
    print("list is out of index")

except:
    print("other error")


print("code after error handling")