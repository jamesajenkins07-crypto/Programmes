values = [1,2,3,4,5]
newValues = list(values)
for i in range(len(values)):
    newValues[i] += 1
    print("Old Value at index {} is: {} ".format(i, values[i]))
    print("New Value at index {} is: {} \n".format(i, newValues[i]))
