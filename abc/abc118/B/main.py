#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    ans = 0
    N, M = map(int, input().split())
    f = [0] * M
    for i in range(N):
        li  = list(map(int, input().split()))[1:]
        for j in range(1, M+1):
            if li.count(j) >= 1:
                f[j-1] += 1

    for i in range(M):
        if f[i] == N:
            ans +=1

    print(ans)
    return

if __name__ == '__main__':
    main()