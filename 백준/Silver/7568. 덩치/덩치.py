N = int(input())
people = []
for n in range(N):
	x, y = list(map(int, input().split()))
	people.append((x,y))
# N명의 집단에서 등수는 자신보다 더 "큰 덩치"의 사람의 수
TF = []
cnt = 0
for i in range(N):
	for j in range(N):
		if people[i][0] < people[j][0]:
			if people[i][1] < people[j][1]:
				cnt += 1
	TF.append(cnt+1)
	cnt = 0
print(*TF,end=' ')