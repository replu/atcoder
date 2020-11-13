#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    H, W, N, M = map(int,input().split())
    f = [[0] * W for i in range(H)]
    for i in range(N):
        x, y = map(int, input().split())
        f[x-1][y-1] = 1
    for i in range(M):
        x, y = map(int, input().split())
        f[x-1][y-1] = -1

    for i in range(H):
        print(f[i])

    x_out = set()
    for i in range(H):
        light = False
        p = 0
        for j in range(W):
            if f[i][j] == -1:
                if not light:
                    for k in range(p, j):
                        x_out.add((i, k))
                p = j+1
                light = False

            if f[i][j] == 1:
                light = True
                p = j+1

        if not light:
            for k in range(p, W):
                x_out.add((i, k))

    y_out = set()
    for i in range(W):
        light = False
        p = 0
        for j in range(H):
            if f[j][i] == -1:
                if not light:
                    for k in range(p, i):
                        y_out.add((k, i))
                p = j+1
                light = False

            if f[j][i] == 1:
                light = True
                p = j+1

        if not light:
            for k in range(p, H):
                y_out.add((k, i))
    print(x_out)
    print(y_out)
    print((H * W) - M - len(x_out & y_out))

if __name__ == '__main__':
    main()
