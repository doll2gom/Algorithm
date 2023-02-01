N = int(input())
num = 666
cnt = 1
while True:
    s_num = str(num)
    if '666' in s_num:
        if cnt == N:
            break
        cnt += 1
    num += 1
print(num)