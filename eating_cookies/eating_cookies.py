def eating_cookies(n):
    '''
    Input: an integer
    Returns: an integer
    '''
    # Your code here
    if n in (0, 1):
        return 1
    if n == 2:
        return 2
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        # This is just the Tribonacci sequence!
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


# def multiply(A, B):
#     '''
#     Input:  A - 3x3 matrix
#             B - 3x3 matrix
#     Output: C - 3x3 matrix product of A and B
#     '''
#     C = [[0]*3]*3
#     for i in range(3):
#         for j in range(3):
#             total = 0
#             for k in range(3):
#                 total = total + A[i][k] * B[k][j]
#             C[i][j] = total
#     return C


# def power(A, n):
#     '''
#     Input:  A - 3x3 matrix
#             n - exponent of matrix
#     Output: ret - the 3x3 matrix A^n
#     '''
#     ret = [[1, 0, 0],
#            [0, 1, 0],
#            [0, 0, 1]]

#     while n > 0:
#         if n & 1:
#             ret = multiply(ret, A)
#         n >>= 1
#         A = multiply(A, A)

#     return ret


# def eating_cookies(n):
#     '''
#     Input: an integer
#     Returns: an integer
#     '''
#     # Your code here
#     Q = [[1, 1, 1],
#          [1, 0, 0],
#          [0, 1, 0]]

#     res = power(Q, n)
#     return res[0][0]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
