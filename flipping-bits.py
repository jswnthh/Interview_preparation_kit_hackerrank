def flippingBits(n):
    str_n = str(n)
    list_bits = [int(x) for x in str_n ]
    for num in list_bits:
        print(num)

n = 0o00000000000000000000000000000001
flippingBits(n)