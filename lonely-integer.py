def lonelyinteger(a):
    #create a frequency dictionary
    freq_dict = {}
    for num in a:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    #get results
    for key, value in freq_dict.items():
        if value == 1:
            lonely_integer = key
            break

    return lonely_integer

a = [1,2,3,4,3,2,1]
result = lonelyinteger(a)
print(result)