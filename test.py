#!/bin/python3

test = "hello world"
insert = '1'
place = "e"
index = test.index(place)

half_test = test[:index]
second_half = test[index + 1:]

new = half_test + insert+ second_half

print(test)
print(half_test)
print(second_half)
print(new)
print(index)
