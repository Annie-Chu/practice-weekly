def removeElement(nums, val: int) -> int:

    for _ in range(len(nums)):
        if val in nums:
            nums.remove(val)

    print(nums)


if __name__ == '__main__':
    removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)