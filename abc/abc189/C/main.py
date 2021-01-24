#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    # al = 0
    # ar = 0
    # ax = 0
    at = 0
    for i in range(N):
        x = A[i]
        f = False
        cl = 0
        cr = 0
        for j in range(N):
            if A[j] < x:
                if f:
                    cl = j
                    at =  max((cl - cr) * x , at)
                f = False
            else:
                if not f:
                    cr = j
                f = True
        if f:
            at =  max((N - cr) * x , at)
    print(at)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
