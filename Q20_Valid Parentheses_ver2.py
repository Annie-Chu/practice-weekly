class Solution:
    def isValid(self, code: str) -> bool:
        character = ['{}', '[]', '()']

        if code == '':
            return True

        if len(code) < 1:
            return False

        if len(code) < 1:
            return False
        else:
            for _ in range(len(code)):
                for a in character:
                    if a in code:
                        code = code.replace(a, '')
                    else:
                        code = code

        return code == ''

if __name__ == '__main__':
    number = Solution()
    results = number.isValid(input('Enter a code: '))
    print(results)