def palindrome(num):
    num_str = str(num)
    rev = num_str[::-1]
    if num_str == rev:
        print('True')

    else:
        print('False')


palindrome(input('Enter a num: '))


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]
