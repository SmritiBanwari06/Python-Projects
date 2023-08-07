with open('CurrencyData.txt') as f:
    lines = f.readlines()
# print(lines)
currencyDict ={}
for line in lines:
    parsed = line.split("\t")
    # print(parsed)
    # break
    currencyDict[parsed[0]] = parsed[1]

# print(currencyDict)
amount = int(input("Enter the amount: "))
print("Enter the name of the currency you want to convert:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these available values: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
    