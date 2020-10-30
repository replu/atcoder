#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, a: "List[int]"):
    n4 = 0
    n2 = 0
    no = 0
    for i in a:
        if i % 4 == 0:
            n4 += 1
        elif i % 2 == 0:
            n2 += 1
        else:
            no += 1
    if n2 > 0:
        no += 1
    if n4+1 >= no:
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
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
