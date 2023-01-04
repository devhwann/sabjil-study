def solution(progresses, speeds):
    answer = []
    day = 0     # 작업 일수 
    count = 0   # 배포된 작업 개수
    
    while len(progresses) > 0:
        # 작업 진도가 100%이상인 경우
        if (progresses[0] + day * speeds[0]) >= 100:
            # 작업 진도(progresses)와 작업 속도(speeds) 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)
            # 배포 개수 1증가
            count +=1
        
        # 작업진도가 100%이상이 아니며 앞에서 배포할 작업이 있는 경우
        else:
            if count > 0:
                # 배포 개수를 리스트에 담고
                answer.append(count)
                # 초기화함
                count = 0
            # 다음 날짜 작업을 확인하기 위해 작업 일수에 하루를 더해줌    
            day += 1
    # 마지막으로 배포된 작업에 대해 append를 실행하지 않고 while문을 빠져나왔음으로 append 해주기
    answer.append(count) 
    
    return answer