def moving_zeroes(arr):
    '''
    Input: a List of integers
    Returns: a List of integers
    '''
    # Your code here
    last_non_zero_idx = 0
    for i, num in enumerate(arr):
        if num != 0:
            arr[last_non_zero_idx], arr[i] = arr[i], arr[last_non_zero_idx]
            last_non_zero_idx += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
