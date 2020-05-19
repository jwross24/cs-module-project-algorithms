from collections import deque


def sliding_window_max(nums, k):
    '''
    Input: a List of integers as well as an integer `k` representing the size of the sliding window
    Returns: a List of integers
    '''
    # Your code here
    deq = deque()
    output = []

    for i, num in enumerate(nums):
        # Pop from the end indices of smaller elements
        while deq and nums[deq[-1]] < num:
            deq.pop()

        # Append the current index
        deq.append(i)

        # Pop from the front the (i - k)th index, if still in the queue
        # This means that it's no longer in the sliding window
        if deq[0] == i - k:
            deq.popleft()

        # Once the window is size k, append the current window maximum to output
        if i + 1 >= k:
            output.append(nums[deq[0]])

    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
