def longestCommonPrefix(strs) -> str:

    new = ''
    num = 0

    if not strs:
        print("")

    for a in strs[0]:
        count = 0
        for i in range(1, len(strs)):

            if a in strs[i] and num < len(strs[i]):
                if strs[0][num] == strs[i][num]:
                    count += 1

            if count == len(strs) - 1:
                new += a

        num += 1

    if new:
        print(new)
    else:
        print('""')


if __name__ == '__main__':

    longestCommonPrefix(["aca", "cba"])