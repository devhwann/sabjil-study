
def solution(s):
    stack = []
    
    for symbol in s:
        if symbol == "(":
            stack.append(symbol)
        # 현재 symbol == ")"인 경우    
        else:
            if stack == []:
                return False
            # 빈 스택이 아닌 경우
            else:
                # stack 맨 끝에 있는 "(" 제거
                stack.pop()

    return stack == []

# s1 = "(())()"             
# s2 = ")()("
# print(solution(s1)) -> True
# print(solution(s2)) -> False
                