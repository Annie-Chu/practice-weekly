def strStr(haystack: str, needle: str) -> int:

    if needle == '':
        return 0

    elif needle not in haystack:
        print(-1)

    else:
        string = haystack.split(needle)
        print(len(string[0]))


if __name__ == '__main__':
    strStr("hello", "ll")