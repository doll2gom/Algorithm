import sys
burger = 2000
beverage = 2000
for _ in range(3):
    input = int(sys.stdin.readline())
    if input < burger:
        burger = input
for _ in range(2):
    input = int(sys.stdin.readline())
    if input < beverage:
        beverage = input
print(burger+ beverage-50)