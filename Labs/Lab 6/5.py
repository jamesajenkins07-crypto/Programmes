def make_dict(groceries):
    groc_dict = {}
    for item in groceries:
        if item[0] not in groc_dict:
            groc_dict[item[0]] = [item]
        else:
            groc_dict[item[0]].append(item)
        
    print(groc_dict)

shopping = ["salami", "cucumber", "cheese", "milk", "salsa"]
make_dict(shopping)
