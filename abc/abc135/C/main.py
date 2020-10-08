#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] = max(0, B[i]-A[i])
        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1]- B[i])
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
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
