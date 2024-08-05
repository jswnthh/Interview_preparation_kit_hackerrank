def plusMinus(arr):
    length_arr = len(arr)
    minus_arr = []
    plus_arr = []
    zero_arr = []
    for i in arr:
        if i < 0:
            minus_arr.append(i)
        elif i > 0:
            plus_arr.append(i)
        else:
            zero_arr.append(i)
    minus_ratio = "{:.6f}".format(len(minus_arr)/(length_arr))
    plus_ratio = "{:.6f}".format(len(plus_arr)/length_arr)
    zero_ratio = "{:.6f}".format(len(zero_arr)/length_arr)

    print(f"{plus_ratio} \n{minus_ratio}\n{zero_ratio}")

arr=[-4, 3, -9, 0, 4, 1]
plusMinus(arr)

