def smallerNumbersThanCurrent(nums):
    small = []
    for i in range(len(nums)):
        count = 0
        for a in range(len(nums)):

            if nums[i] > nums[a]:
                count += 1

        small.append(count)

    print(small)


if __name__ == '__main__':
    smallerNumbersThanCurrent([7, 7, 7, 7])