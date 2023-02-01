l = []
for n in range(1,int(input())+1):
    str_n = str(n)
    for s in str_n:
        if s == '4' or s == '7':
            if str_n.count('4') + str_n.count('7') == len(str_n):
                l.append(n)
print(l[-1])