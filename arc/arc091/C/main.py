#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    if N == 1 and M == 1:
        print(1)
    elif N == 1 or M == 1:
        print(max(N, M)-2)
    else:
        print((N * M) - (2*N) - (2 * M) + 4)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
