#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = A[0]
    m = 0
    for i in range(2, max(A) + 1):
        c = 0
        for j in range(N):
            if A[j] % i == 0 and i <= A[j]:
                c += 1
        if c > m:
            m = c
            ans = i
    print(ans)




if __name__ == '__main__':
    main()
