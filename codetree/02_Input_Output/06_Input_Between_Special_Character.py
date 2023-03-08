# 1
a = input().split(":")
print(int(a[0])+1, ":", int(a[1]), sep="")

# 2
m, d, y = input().split("-")
print(f"{y}.{m}.{d}")

# 3
a = input().split("-")
print(f'{a[0]}{a[1]}')

# 4
y, m, d = input().split('.')
print(f"{m}-{d}-{y}")

# 5
y, m, d = input().split('-')
print(f"{y}-{d}-{m}")
