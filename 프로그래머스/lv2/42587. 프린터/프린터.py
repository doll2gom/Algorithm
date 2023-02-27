from collections import deque

def solution(priorities, location):
    printer = [ (i,p) for i,p in enumerate(priorities)]
    answer = 0
    while printer:
        first = printer.pop(0)
        if any(first[1] < other[1] for other in printer):
            printer.append(first)
        else:
            answer += 1
            if first[0] == location: 
                break
            
    return answer