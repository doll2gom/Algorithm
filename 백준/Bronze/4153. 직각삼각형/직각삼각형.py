while True:
    lst = list(map(int, input().split()))
    a = max(lst)
    if sum(lst) == 0:
        break
    lst.remove(a)
    if lst[0] ** 2 + lst[1] ** 2 == a ** 2:
        print("right")
    else:
        print("wrong")