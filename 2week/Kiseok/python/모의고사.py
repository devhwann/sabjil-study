def solution(answers):
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    answer = []
    
    f_ans=first*(len(answers)//len(first))+first[0:len(answers)%len(first)]
    s_ans=second*(len(answers)//len(second))+second[0:len(answers)%len(second)]
    t_ans=third*(len(answers)//len(third))+third[0:len(answers)%len(third)]
           
    for ans in [f_ans,s_ans,t_ans]:
        tmpscore=0
        for i in range(len(ans)):
            if answers[i]==ans[i]:
                tmpscore+=1
        answer.append(tmpscore)
    return [i+1 for i in range(3) if answer[i]==max(answer)]