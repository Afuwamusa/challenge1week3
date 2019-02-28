def sort(num):
#creating empty dictionary
    dict = {}
#creating empty lists that will hold the sorted characters.
    even = []
    odd = []
    chars = []
#looking for the sorted  characters to append in the empty lists created
    for x in num:
#checking  wether integers exist in the function
        if isinstance(x, int):
            if x %2 ==0:
                even.append(x)
            elif x %2 != 0:
                odd.append(x)
#checking wether floats exist
        elif isinstance(x, float):
            if x %2 !=0:
                odd.append(x)
            elif x %2 ==0:
                even.append(x)
#checking wether strings exist
        elif isinstance(x, str):
            chars.append(x)
#adding keys and sorted values to the dictionary
    dict["even"] =sorted(even) 
    dict["odd"] =sorted(odd) 
    dict["chars"] =sorted(chars)
#returning the dictionary 
    return dict
#calling for the function
print(sort([2,3,4,5,6,7,8,9,3.1,4.2,"a","b","c"]))