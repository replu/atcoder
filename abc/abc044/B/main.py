#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(w: str):
    base = ord('a')
    b = [0] * 26
    for s in w:
        b[ord(s)- base] += 1
    for i in b:
        if i % 2 != 0:
            print(NO)
            return

    print(YES)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    w = next(tokens)  # type: str
    solve(w)

if __name__ == '__main__':
    main()