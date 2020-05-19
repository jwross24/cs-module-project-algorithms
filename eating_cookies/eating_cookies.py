


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


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
