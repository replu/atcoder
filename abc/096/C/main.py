#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, S: "List[str]"):
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                continue
            if i - 1 >= 0:
                if S[i - 1][j] == "#":
                    continue
            if i + 1 < H:
                if S[i + 1][j] == "#":
                    continue
            if j - 1 >= 0 and S[i][j - 1] == "#":
                continue
            if j + 1 < W and S[i][j + 1] == "#":
                continue
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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [list(next(tokens)) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == "__main__":
    main()
