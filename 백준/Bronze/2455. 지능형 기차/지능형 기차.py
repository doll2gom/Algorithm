max_train = 0
people_cnt = 0
# 기차역은 4개로 정해져 있다.
for station in range(4):
	on, off = map(int, input().split())
	people_cnt -= on
	people_cnt += off
	if people_cnt > max_train:
		max_train = people_cnt
print(max_train)