def longestCommonPrefix(strs) -> str:

    new = ''

    if not strs:
        print("")

    for i in range(len(min(strs, key=len))):
        count = 0
        for num in range(1, len(strs)):
            if strs[0][i] == strs[num][i]:
                count += 1

        if count == len(strs) - 1:
            new += strs[0][i]

        else:
            break

    if new:
        print(new)
    else:
        print('""')


if __name__ == '__main__':

    longestCommonPrefix(["flower","flow","flight"])