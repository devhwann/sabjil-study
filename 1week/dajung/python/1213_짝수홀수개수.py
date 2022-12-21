def solution(num_list):
    answer = []
    even = []
    odd = []
    for i in num_list:
        #짝수일 때
        if i%2 == 0:
            even.append(i);
        #홀수일 때
        else:
            odd.append(i);
    answer.append(len(even))
    answer.append(len(odd))    
    return answer