def squareRoot(number, precision):
    start = 0
    end, ans = number, 1
    while (start <= end):
        mid = int((start + end) / 2)

        if (mid * mid == number):
            ans = mid
            break
        if (mid * mid < number):
            start = mid + 1
            ans = mid

        else:
            end = mid - 1

    increment = 0.1
    for i in range(precision):
        while (ans * ans <= number):
            ans += increment

        # loop terminates when ans * ans > number
        ans = ans - increment
        increment = increment / 10

    return ans


# Driver code
print(round(squareRoot(50, 3), 4))
print(round(squareRoot(10, 4), 4))


def nextPerm(nums):
    # n=len(num)
    # pivot=-1
    # i=n-2
    # while i>-1:
    #     if num[i]<num[i+1]:
    #         break
    #     i-=1

    # if i==-1:
    #     num.reverse()
    #     return
    # pivot=i
    # nextpivot=None
    # for i in range(pivot+1,n):
    #     if num[i]>num[pivot]:
    #         nextpivot=i

    # num[pivot],num[nextpivot]=num[nextpivot],num[pivot]
    # num[pivot+1:]=reversed(num[pivot+1:])
    # def next_permutation(nums):
    i = len(nums) - 2

    while i >= 0:
        if nums[i] < nums[i + 1]:
            break
        i -= 1

    if i < 0:
        nums.sort()
    else:
        swap_val = nums[i + 1]
        idx = i + 1
        for j in range(i + 1, len(nums)):
            if nums[j] < swap_val and nums[j] > nums[i]:
                swap_val = nums[j]
                idx = j

        nums[i], nums[idx] = nums[idx], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])

    return nums


# # Example usage
# nums = [1, 2, 3, 4, 5, 7, 6, 3]
# result = next_permutation(nums)
# print(result)

a = [2, 2, 4, 6, 7, 3, 6]
nextPerm(a)
print(a)

from collections import deque


def oranges(grid):
    if not grid:
        return -1

    row, col = len(grid), len(grid[0])
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    fresh = 0
    q = deque()
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                q.append((i, j))

    minutes = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            cx = x + dx
            cy = y + dy
            if 0 <= cx < row and 0 <= cy < col and grid[i][j] == 1:
                q.append((cx, cy))
                grid[i][j] = 2
                fresh -= 1
        minutes += 1

    return minutes - 1 if fresh == 0 else -1


def median(matrix):
    m = len(matrix)
    n = len(matrix[0])
    low = matrix[0][0]
    high = matrix[-1][-1]
    while low <= high:
        mid = low + (high - low) // 2
        left_count = bisect_left()
        count = 0
        j = n - 1
        for i in range(m):
            while j > -1 and matrix[i][j] < mid:


                if count < (m * n) // 2:
                    low = mid + 1
                else:
                    high = mid - 1
            return mid