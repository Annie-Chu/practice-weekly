def one(x):

    if x == 0:
        print(0)

    while (x % 10) == 0:
        x = x // 10

    if x > 0:
        comp = int(str(x)[::-1])
        if comp > (2 ** 31) - 1:
            print(0)
        else:
            print(comp)

    if x < 0:
        comp = -(int(str(x)[:0:-1]))
        if comp < -(2 ** 31):
            print(0)
        else:
            print(comp)


if __name__ == '__main__':
    one(12300)