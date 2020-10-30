#!/usr/bin/env python3
import sys


def solve(n: int, s: str, t: str):
    ls = len(s)
    lt = len(t)
    if ls + lt == n:
        print(ls+lt)
    elif ls + lt < n:
        lp = n - ls - lt
        print(ls + lp + lt)
    else:
        for i in range(ls, 0, -1):
            if s[-i:] == t[:i]:
                print(ls + lt -i)
                return
        print(ls+lt)
    return


# generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: you use the default template now. you can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(n, s, t)

if __name__ == '__main__':
    main()
