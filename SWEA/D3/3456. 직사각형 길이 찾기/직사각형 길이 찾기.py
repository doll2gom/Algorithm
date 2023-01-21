T = int(input())
for test_case in range(1, T+1):
    numbers = input().split()
    for n in numbers:
        if numbers.count(n) == 1:
            print(f'#{test_case} {n}')
        elif numbers.count(n) == 3:
            print(f'#{test_case} {n}')
            numbers.clear()