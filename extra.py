def find(missing):
    missing_numbers =[]
    for y in range(0,10):
        if y not in missing:
            missing_numbers.append(y)
    return missing_numbers
print(find([1,3,5,7,9]))       
