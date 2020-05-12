def two(target, nums):

    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in nums and nums.index(comp) != i:
            print([i, nums.index(comp)])


if __name__ == '__main__':
    two(10, [2, 5, 5, 11])

