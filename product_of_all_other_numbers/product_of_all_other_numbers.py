def product_of_all_other_numbers(arr):
    '''
    Input: a List of integers
    Returns: a List of integers
    '''
    # Your code here
    # Length of the input array
    length = len(arr)

    # The answer array that we return
    answer = [0]*length

    # answer[i] holds the product of all the elements to the left
    answer[0] = 1  # no elements to the left, so product is 1
    for i in range(1, length):
        answer[i] = arr[i - 1] * answer[i - 1]

    # This solution uses O(1) space and calculates R on-the-fly
    # R holds the product of all the elements to the right
    R = 1  # no elements to the right, so product is 1
    for i in reversed(range(length)):  # range(length - 1, -1, -1)
        answer[i] = answer[i] * R
        # Update R
        R *= arr[i]

    return answer


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
