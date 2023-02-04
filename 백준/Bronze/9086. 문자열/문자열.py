T = int(input())
a = [ list(map(str, input())) for _ in range(T)]
for t in range(T):
    print(f'{a[t][0]}{a[t][-1]}')