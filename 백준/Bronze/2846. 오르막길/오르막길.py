M = int(input()) # M과 M번 측정한 높이들을 입력받는다.
way = list(map(int, input().split()))

lst = [] # 리스트를 준비해 모든 오르막길의 높이를 모은다.
cnt = 0  # 이동한 거리를 카운트하여 오르막길의 시작과 끝의 인덱스를 특정
for h in range(0,M): # 측정한 횟수만큼 반복하며 알아본다.
    if way[h] < way[(h+1)%M]:      # 현위치 vs 앞위치 오르막의 끝인지 확인
        cnt += 1 # 이동거리를 카운트   #(h+1)%M는 인덱스 범위를 넘어서지 않기 위한 장치이다.
    elif way[h] >= way[(h+1)%M]:   # 오르막의 끝이라면
        high = way[h] - way[h-cnt] # 현위치에서 오르막이 시작한 지점의 높이를 빼기
        lst.append(high)           # 구한 오르막의 높이를 리스트에 모은다.
        cnt = 0  # 오르막 이동거리 0으로 초기화
print(max(lst))  # 오르막 높이 모음에서 최댓값 출력