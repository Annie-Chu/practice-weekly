def addBinary(a: str, b: str) -> str:
    n1 = len(a) - 1
    n2 = len(b) - 1
    cal = 0
    ans = []

    while n1 >= 0 or n2 >= 0 or cal is not 0:
        if n1 >= 0:
            cal += int(a[n1])
            n1 -= 1

        if n2 >= 0:
            cal += int(b[n2])
            n2 -= 1

        ans.append(str(cal % 2))
        cal //= 2

    print(''.join(reversed(ans)))


if __name__ == '__main__':
    addBinary('1010', '1011')