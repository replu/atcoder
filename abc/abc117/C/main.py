#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: "List[int]"):
    if N >= M:
        print(0)
        return
    x = sorted(X)
    d = []
    a = x[0]
    for i in range(1, M):
        d.append(abs(a - x[i]))
        a = x[i]

    d = sorted(d)
    print(sum(d[0:len(d)-N+1]))



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
    X = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X)

if __name__ == '__main__':
    main()
