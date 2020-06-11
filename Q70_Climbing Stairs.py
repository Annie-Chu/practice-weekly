def climbStairs(n: int) -> int:

    ans = [1, 2]
    a = 2

    if n is 1:
        return ans[0]
    elif n is 2:
        return ans[1]

    else:
        for i in range(0, n - 2):
            a += ans[i]
            ans.append(a)

        return ans[-1]


if __name__ == '__main__':
    ans1 = climbStairs(7)
    print(ans1)