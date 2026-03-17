#!/bin/python3

num_list = []

while len(num_list) < 10:
    num = int(input(f"Please enter {10 - len(num_list)} unique numbers: "))
    if num not in num_list:
        num_list.append(num)

print(num_list)
