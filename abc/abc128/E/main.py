#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, S: "List[int]", T: "List[int]", X: "List[int]", D: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
    D = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, S, T, X, D)

if __name__ == '__main__':
    main()
