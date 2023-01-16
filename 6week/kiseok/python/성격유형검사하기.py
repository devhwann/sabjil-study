# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    pdict={
        'R':0,'T':0,'C':0,'F':0,"J":0,"M":0,"A":0,"N":0
    }
    for i in range(len(survey)):
        if choices[i]>4:
            pdict[survey[i][1]]+=(choices[i]-4)
        elif choices[i]<4:
            pdict[survey[i][0]]+=(4-choices[i])
    for i in range(4):
        f,s=list(pdict.keys())[2*i],list(pdict.keys())[2*i+1]
        if pdict[f]<pdict[s]:
            answer+=s
        else:
            answer+=f
    return answer
