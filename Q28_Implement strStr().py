def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0

    if needle in haystack:
        print(haystack.index(needle))

    else:
        print(-1)


if __name__ == '__main__':
    strStr("hello", "ll")