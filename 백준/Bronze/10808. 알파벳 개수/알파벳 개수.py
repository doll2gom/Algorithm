import sys
s = sys.stdin.readline()
string = [ chr(i) for i in range(97, 123)]
lst = [ 0 for _ in range(26)]
for i in s:
    try:
        lst[string.index(i)] += 1
    except:
        break
print(*lst)
