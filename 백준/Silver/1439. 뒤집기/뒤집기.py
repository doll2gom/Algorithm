import sys
words = sys.stdin.readline()
cnt0 = 0
cnt1 = 0
change = '2'

for i in words:
    if i != change:
        if i == '0':
            cnt0 += 1
            change = '0'
        elif i == '1':
            cnt1 += 1
            change = '1'
print(min(cnt0, cnt1))