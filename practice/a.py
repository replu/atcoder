# vim: fileencoding=utf-8


def main():
    a = int(input())
    b, c = map(int, input().split())
    s = input()
    print(f"{a + b + c} {s}")


if __name__ == "__main__":
    main()
