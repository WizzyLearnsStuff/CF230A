
def main():
    s, n = tuple(map(int, input().split()))

    dragons = []
    for i in range(n):
        dragons.append(tuple(map(int, input().split())))

    dragons.sort(key=lambda i: i[0])

    for st, bo in dragons:
        if s <= st:
            print("NO")
            return
        s += bo

    print("YES")

main()
