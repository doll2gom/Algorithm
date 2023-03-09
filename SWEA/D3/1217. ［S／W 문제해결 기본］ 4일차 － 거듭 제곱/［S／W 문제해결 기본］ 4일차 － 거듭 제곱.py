def rcrs(n, m): 
    if m == 1: 
        return n 
    elif m >= 2:  
        return n * rcrs(n, m-1)

while True:
    try:
        t = int(input())
        n, m = map(int, input().split())
        print(f"#{t} {rcrs(n, m)}")
    except:
        break