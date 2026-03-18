#!/bin/python3

values =[1,2,3,4,5,"hello",6,7,8,9,"10"]
for cur in values:
    print("The value is :", values[cur])
    if type(values[cur]) == str:
        print("This is a string!")
