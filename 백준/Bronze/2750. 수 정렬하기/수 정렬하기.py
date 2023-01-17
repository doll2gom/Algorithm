numbers = []
T = int(input())
for n in range(1,T+1):
    n = int(input())
    if n not in numbers:
        numbers.append(n)
    numbers.sort()
for number in numbers:
    print(number)