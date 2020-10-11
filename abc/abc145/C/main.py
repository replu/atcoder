#!/usr/bin/env python3
import sys
import itertools
import math


def solve(N: int, x: "List[int]", y: "List[int]"):
    l = list(range(N))
    d = 0

    p_list = list(itertools.permutations(l, N))
    for p in p_list:
        t = 0
        for i in range(N-1):
            t += math.sqrt( (x[p[i]]-x[p[i+1]]) ** 2 + (y[p[i]]-y[p[i+1]]) ** 2)
        d += t
    print(d/len(p_list))
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()