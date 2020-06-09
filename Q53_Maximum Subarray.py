def maxSubArray(nums) -> int:
    ans = nums[0]
    total = nums[0]
    a = []
    for i in range(1, len(nums)):
        t1 = nums[i] + total
        print(t1)
        if t1 < nums[i]:
            total = nums[i]
            a.append(total)
        else:
            total = t1
            a.append(total)

        ans = max(ans, total)

    print(ans)
    print(a)


if __name__ == '__main__':
    maxSubArray([1, 3, -1, -5])