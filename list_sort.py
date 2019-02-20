def sort(list):
#creating empty dictionary
    dict = {}
    even = []
    odd = []
    chars = []
    for x in list:
        if isinstance(x, int):
            if x %2 ==0:
                even.append(x)
            elif x %2 != 0:
                odd.append(x)
        elif isinstance(x, float):
            if x %2 !=0:
                odd.append(x)
            elif x %2 ==0:
                even.append(x)
        elif isinstance(x, str):
            chars.append(x)
    dict["even"] =sorted(even) 
    dict["odd"] =sorted(odd) 
    dict["chars"] =sorted(chars) 
    return dict
#calling for the function
print(sort([2,3,4,5,6,7,8,9,3.1,4.2,"a","b","c"]))