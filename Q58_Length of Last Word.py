def lengthOfLastWord(s: str) -> int:
    word = []
    for i in s:
        word.append(i)

    if ' ' in word:
        if word[-1] is ' ':
            count = 0
            for i in range(len(word)-2, -1, -1):
                if word[i] is not ' ':
                    count += 1
                    if word[i-1] is ' ':
                        break
            print(count)

        else:
            for i in range(len(word)-1, -1, -1):
                if word[i] is ' ':
                    print(len(word) - 1 - i)
                    break
    else:
        print(len(word))


if __name__ == '__main__':
    lengthOfLastWord(' bac  ')
