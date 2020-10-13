#!/usr/bin/env python3
import sys


def solve(S: str):
    c = 0
    ans = 0
    for i in range(len(S)-1, 0-1, -1):
        if S[i] == 'B':
            ans += len(S) - i - c -1
            c += 1
    print(ans)


    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
