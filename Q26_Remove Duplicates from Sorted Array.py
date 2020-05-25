def removeDuplicates(nums) -> int:
    i = 0

    if nums:
        while i + 1 < len(nums):

            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
                i = i

            else:
                i += 1

    else:
        print([])


if __name__ == '__main__':
    removeDuplicates([])