import sys
n = int(sys.stdin.readline())
files = {}
for _ in range(n):
    file = list(map(str, sys.stdin.readline().split('.')))[1]
    file = file.strip('\n')
    if file not in files:
        files[file] = 1
    else:
        files[file] = files.get(file) + 1
for f in sorted(files):
    print(f, files[f])
