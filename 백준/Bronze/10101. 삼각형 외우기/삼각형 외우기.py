l = []
for i in range(0,3):
    l.append(int(input()))
if l[0] == l[1] == l[2] == 60:
    print('Equilateral')
elif sum(l) == 180:
    if l[0] == l[1] and l[0] != l[2]:
        print('Isosceles')
    elif l[0] == l[2] and l[0] != l[1]:
        print('Isosceles')
    elif l[1] == l[2] and l[0] != l[1]:
        print('Isosceles')
    elif l[0] != l[1] != l[2]:
        print('Scalene')
elif sum(l) != 180:
    print('Error')