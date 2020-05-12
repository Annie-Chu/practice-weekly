def roman(romans):
    romans = str(romans).upper()
    out = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    a = 0

    for key in out.keys():
        if key in romans:
            a += out[key]
            romans = romans.replace('{}'.format(key), '')

    for ii in romans:
        if ii in symbol.keys():
            a += symbol[ii]
            romans = romans.replace('{}'.format(ii), '')

    print(a)


if __name__ == '__main__':
    roman(input('Enter Roman: '))
