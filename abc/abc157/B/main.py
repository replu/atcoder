#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    for i in range(N):
        n = b[i]
        for j in range(3):
            for k in range(3):
                if A[j][k] == n:
                    A[j][k] = 0
    if A[0][0] == A[0][1] == A[0][2]:
        print(YES)
    elif A[1][0] == A[1][1] == A[1][2]:
        print(YES)
    elif A[2][0] == A[2][1] == A[2][2]:
        print(YES)
    elif A[0][0] == A[1][0] == A[2][0]:
        print(YES)
    elif A[0][1] == A[1][1] == A[2][1]:
        print(YES)
    elif A[0][2] == A[1][2] == A[2][2]:
        print(YES)
    elif A[0][0] == A[1][1] == A[2][2]:
        print(YES)
    elif A[0][2] == A[1][1] == A[2][0]:
        print(YES)
    else:
        print(NO)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()