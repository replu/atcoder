#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    A.sort()
    sum = [0] * N
    sum[N-1] = A[N-1]
    for i in range(N-2, -1, -1):
        sum[i] = sum[i+1] + A[i]

    ans = 0

    for i in range(N-1):
        ans += sum[i+1] - (A[i] * (N-1-i))
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
