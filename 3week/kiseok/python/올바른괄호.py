# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    idx_dict={"(":[],")":[]}
    for i in range(len(s)):
        idx_dict[s[i]].append(i)
    
    #두 부호의 개수가 다르면 false
    if len(idx_dict["("])!=len(idx_dict[")"]):
        return False
    
    
    idx_dict["("]=list(reversed(idx_dict["("]))
    idx_dict[")"]=list(reversed(idx_dict[")"]))

    for i in range(len(idx_dict["("])):
        o,c=idx_dict["("][i],idx_dict[")"][i]
        if o>c:
            return False
    
    return True