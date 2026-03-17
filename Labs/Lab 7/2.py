#!/bin/python3

sales_data = open("sales_data.tsv", "r")
total_apples = 0
apple_best = 0
total_bananas = 0
banana_best = 0
total_oranges = 0
orange_best = 0

for line in sales_data:
    info = line.split("\t")
    fruit = info[0].strip()
    amount = int(info[2].strip())
    day = info[1].strip()

    if fruit == "Apple":
        total_apples += amount

        if amount > apple_best:
            apple_best = amount
            apple_day = day

    elif fruit == "Banana":
        total_bananas += amount

        if amount > banana_best:
            banana_best = amount
            banana_day = day

    elif fruit == "Orange":
        total_oranges += amount

        if amount > orange_best:
            orange_best = amount
            orange_day = day

sales_data.close()

print("Total sales per product:")
print("Apple:", total_apples, "units")
print("Banana:", total_bananas, "units")
print("Orange:", total_oranges, "units")
print("")
print("Highest sales days:")
print(f"Apple: {apple_day} ({apple_best} units)")
print(f"Banana: {banana_day} ({banana_best} units)")
print(f"Orange: {orange_day} ({orange_best} units)")
