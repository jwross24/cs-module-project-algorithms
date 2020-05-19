from functools import reduce


def single_number(arr):
    '''
    Input: a List of integers where every int except one shows up twice
    Returns: an integer
    '''
    # Your code here
    return reduce(lambda x, y: x ^ y, arr)


# def single_number(arr):
#     '''
#     Input: a List of integers where every int except one shows up twice
#     Returns: an integer
#     '''
#     # Your code here
#     seen = set()

#     for num in arr:
#         if num in seen:
#             seen.remove(num)
#         else:
#             seen.add(num)

#     return seen.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
