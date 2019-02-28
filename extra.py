#creating a function 
def find(missing):
#creating an empty list that will hold the  missing numbers
    missing_numbers =[]
#looking for the missing numbers in the list and appending them to the empty list
    for y in range(0,10):
        if y not in missing:
            missing_numbers.append(y)
#returnng the missing numbers.
    return missing_numbers
print(find([1,3,5,7,9]))       
