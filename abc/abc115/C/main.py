#!/usr/bin/env python3
import sys


def solve(N: int, K: int, h: "List[int]"):
    h.sort()
    ans = float('inf')
    for i in range(0, N-K+1):
        t = h[i+K-1]- h[i]
        if ans > t:
            ans = t
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()
