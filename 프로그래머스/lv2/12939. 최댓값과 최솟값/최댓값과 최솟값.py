def solution(s):
    s = s.split(" ")
    mn = int(s[0])
    mx = int(s[0])
    for i in s:
        i = int(i)
        if i < mn:
            mn = i
        if i > mx:
            mx = i
    answer = str(mn) + " " + str(mx)
    return answer