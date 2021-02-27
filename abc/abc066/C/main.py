#!/usr/bin/env python3
import sys


def solve(n: int, a: "List[str]"):
    odd = []
    even = []
    if n % 2 == 0:
        for i in range(0, n, 2):
            even.append(a[i])

        for i in range(n-1, 0, -2):
            odd.append(a[i])
        ans = odd + even
    else:
        for i in range(n-1, -1, -2):
            even.append(a[i])

        for i in range(1, n, 2):
            odd.append(a[i])
        ans = even + odd

    print(' '.join(ans))

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [next(tokens) for _ in range(n)]  # type: "List[str]"
    solve(n, a)

if __name__ == '__main__':
    main()
