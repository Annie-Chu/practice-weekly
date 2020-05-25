def removeElement(nums, val: int) -> int:
    n = 0
    x = 0

    if nums:
        for i in range(len(nums)):
            if val != nums[i]:
                nums[n], nums[i] = nums[i], nums[n]
                n += 1
                x += 1
        print(x)
        print(nums)

    else:
        print([])


if __name__ == '__main__':
    removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)