
def searchInsert(nums, target) -> int:
    mid_num = len(nums)//2
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                print(i)
                break
            else:
                i += 1

    else:

        if nums[mid_num] < target:
            for i in range(mid_num, len(nums)):
                if i < len(nums) - 1:
                    if nums[i] == target:
                        print(i)
                    if nums[i] < target < nums[i+1]:
                        print(i + 1)
                        break
                else:
                    if nums[i] == target:
                        print(i)
                    elif nums[i] > target:
                        print(i)
                    else:
                        print(i + 1)

        else:
            for i in range(mid_num, -1, -1):
                if i > 0:
                    if nums[i] == target:
                        print(i)
                    if nums[i] < target < nums[i+1]:
                        print(i + 1)
                        break
                else:
                    if nums[i] == target:
                        print(i)
                    elif nums[i] > target:
                        print(i)
                    else:
                        print(i + 1)


if __name__ == '__main__':
    searchInsert([1, 3, 5, 9, 10], 8)
