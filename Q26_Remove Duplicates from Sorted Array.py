def removeDuplicates(nums) -> int:
    i = 0

    while i + 1 < len(nums):

        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
            i = i

        else:
            i += 1

    print(nums)


if __name__ == '__main__':
    removeDuplicates([1, 2])