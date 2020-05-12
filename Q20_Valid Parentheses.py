class Solution:
    def isValid(self, code: str) -> bool:
        left = ['{', '(', '[']
        right = ['}', ')', ']']
        n1 = []
        n2 = []

        for i in left:
            if i in code:
                num1 = code.find(i)
                n1.append(num1+1)
            else:
                n1.append(0)

        for a in right:
            if a in code:
                num2 = code.find(a)
                n2.append(num2+1)
            else:
                n2.append(0)

        print(n1)
        print(n2)

        for i in range(3):
            if n2[i] != 0 and n1[i] != 0:
                count = n2[i] - n1[i] + 1
                return count % 2 == 0

if __name__ == '__main__':
    number = Solution()
    results = number.isValid(input('Enter a code: '))
    print(results)