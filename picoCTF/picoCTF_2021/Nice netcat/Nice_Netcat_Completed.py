def netCat(numbs):
    flag=""
    for num in numbs:
        result=chr(num)
        flag+= result
    return(flag)
list=[112,105,99,111,67,84,70,123,103,48,48,100,95,107,49,116,116,121,33,95,110,49,99,51,95,107,49,116,116,121,33,95,102,50,100,55,99,97,102,97,125,10] 

print(netCat(list))

