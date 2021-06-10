try:
    a = 2 + 'w'
except:
    # print("error happen")
    pass

# print("command after error")

adresses = {"fahmi":"Bekasi", "Yessy":"Citayeum"}

try:
    result = adresses["Aswin"]
except:
    result = None

# print(result)

try:
    tan = 100/0
except:
    tan = float('inf')

# print(type(tan), tan)

try:
    # a = 2 + 'w'

    # tan = 100/0

    result = adresses["Aswin"]

    print("inside try block")

except TypeError:
    print("something wrong with operation")

except ZeroDivisionError:
    print("tan is infinite")
    tan = float('inf')

except:
    print("another type of error")

