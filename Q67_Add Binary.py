def addBinary(a: str, b: str) -> str:
    n1 = int(a, 2)
    n2 = int(b, 2)

    n3 = bin(n1 + n2)[2:]

    print(n3)


if __name__ == '__main__':
    addBinary('11', '1')