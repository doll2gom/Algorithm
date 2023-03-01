while True:
    a, b = map(int, input().split())
    if a == 0 == b:
        break
    if a > b:
        print("Yes")
    else:
        print("No")