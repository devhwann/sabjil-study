# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    answer = []
    tmp_dict={}
    for i in numlist:
        len=abs(i-n)
        if len not in tmp_dict:
            tmp_dict[len]=[i]
        else:
            tmp_dict[len].append(i)
            
    for i in sorted(tmp_dict.keys()):
        for j in sorted(tmp_dict[i], reverse=True):
            answer.append(j)
            
    return answer