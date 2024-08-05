def miniMaxSum(arr):
    total_sum = sum(arr)
    print('total_sum', total_sum)
    min_sum = float('inf')
    max_sum = float('-inf')

    for num in arr:
        print('num', num)
        current_sum = total_sum - num
        print('current_sum', current_sum)
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum

    print(f"{min_sum} {max_sum}")

# Example usage
arr = [1,3,5,7,9]
miniMaxSum(arr)