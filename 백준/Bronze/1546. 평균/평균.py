lst = []
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
for score in scores:
    lst.append(score/M*100)
print(sum(lst)/len(scores))