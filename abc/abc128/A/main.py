#!/usr/bin/env python3
import sys


def solve(A: int, P: int):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(A, P)

if __name__ == '__main__':
    main()
