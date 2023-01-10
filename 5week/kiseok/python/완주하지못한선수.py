# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    person_dict={}
    
    for i in participant:
        if i not in person_dict:
            person_dict[i]=1
        else:
            person_dict[i]+=1
            
    for i in completion:
        person_dict[i]-=1
        if person_dict[i]==0:
            del person_dict[i]
            
    return list(person_dict)[0]