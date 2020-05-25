def removeDuplicates(nums) -> int:

    x = 1
    n = 1

    if nums:
        a = nums[0]

        for i in range(1, len(nums)):
            if a != nums[i]:
                a = nums[i]
                nums[n], nums[i] = nums[i], nums[n]
                n += 1
                x += 1
        print(x)
        print(nums)

    else:
        print([])


if __name__ == '__main__':
    removeDuplicates([])