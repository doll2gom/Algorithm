num = ''
while True:
    try:
        num += input()
    except EOFError:
        break
print(sum(map(int, num.split(','))))