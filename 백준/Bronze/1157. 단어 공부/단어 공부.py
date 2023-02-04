A = input().upper()
A_list = list(set(A))
lst = []
for a in A_list:
    lst.append(A.count(a))
if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(A_list[lst.index(max(lst))])