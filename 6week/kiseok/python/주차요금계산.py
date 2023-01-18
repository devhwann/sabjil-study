# https://school.programmers.co.kr/learn/courses/30/lessons/92341

# ceil함수(올림 함수)를 이용하기 위하여 math 라이브러리를 import했습니다.
# 가급적 지양하는 부분인데 이것만 구현하려고 코드를 작성하면 코드가 더 지저분해져서 import했습니다.
import math
def solution(fees, records):
    # 초기설정값.
    answer = []
    parking_dict={}

    # 해당 for문을 통해 parking_dict라는 dictionary구조에 차의번호:[출입시간리스트] 와 같은 형태로 저장합니다.
    # dictionary구조는 JS의 오브젝트 타입의 저장방식과 유사하다고 생각하시면 됩니다. 
    for i in records:
        # records의 각 요소를 split()하여 분할된 요소를 각각 time, num, option에 저장합니다.
        time,num,option =i.split()
        # parking_dict에 num이라는 key가 존재하지 않는다면 처음으로 차량번호와 입차시간을 저장합니다.
        if num not in parking_dict:
            parking_dict[num]=[time]
        # parking_dict에 num이라는 key가 존재한다면 출입시간 리스트에 계속해서 시간을 추가로 저장해줍니다.
        else:
            parking_dict[num].append(time)

    # 해당 for문으로 시간에 따른 금액을 계산합니다.
    # dictionary타입의 keys()함수는 각 key들을 리스트로 반환하며 sorted()함수를 통해 키를 오름차순으로 정렬해줍니다.
    # 주의하셔야할 점은 key의 형태가 문자열이라는 점입니다.
    # 그러나 차량번호의 자리수는 4자리로 동일하며 각자리는 숫자임으로 sorted에서도 숫자형의 그것과 동일한 결과를 가져옵니다.
    for i in sorted(parking_dict.keys()):
        # parking_dict에 num을 key로 갖는 출입시간 리스트의 길이가 홀수라면,
        # 차량이 out된 시간이 저장되지 않은 것임으로 리스트에 '23:59'를 추가해줍니다.
        if len(parking_dict[i])%2!=0:
            parking_dict[i].append('23:59')

        # 죄송합니다..!
        # 아래부터 함수가 지저분할 수 있습니다..! 혹시나 모르는 부분이 있다면 코멘트해주시면 답변하겠습니다! 
        # map함수는 JS와 크게 다르지 않습니다.
        # map({함수},{인자})를 이용하면 해당 인자에 함수를 적용시킨값을 순차적으로 반환해줍니다.
        # 함수의 경우 lambda함수(익명함수)를 이용하며, 해당 함수의 표현식은 아래와 같습니다.
        # lambda x: x+2 ===> 다음 함수는 JS의 arrow function으로 표현하면 아래와 같습니다.
        # (x)=>{return x+2} 들어가는 매개변수가 여럿일 경우 lambda x,y : x-y 등으로 나타내면 되겠습니다.
        
        # 그렇다면 아래 함수는 들어가는 인자 x에 대하여 split(':')을 통해 시와 분 단위로 해당 값을 분해하고,
        # 0번째 인덱스에 60을 곱해 시간을 분단위로 나타내고 1번째 인덱스를 더해 결국 시간을 분단위로 환산해주었습니다.

        # map({함수},{인자})에서 인자값의 경우 parking_dict[i][1::2]라고 정의되어 있습니다.
        # parking_dict[i]는 리스트 형태입니다. list[n::x]를 이해해야 합니다.
        # list[n::x]는 n번째 인덱스부터 x만큼 건너뛴 인덱스의 요소들을 반환합니다.
        # 예를들어 list[1::3] = [list[1],list[1+3],list[1+2*3],...]과 같은 형태로 나타나는 것입니다.

        # 홀수번째로 들어온 리스트요소들은 입차시간입니다. 반대로 짝수번째로 들어온 요소들은 출차시간입니다.
        # 각 요소들의 차이는 결국 (출차시간의 분단위환산의 총합) - (입차시간의 분단위 환산의 총합) = (차량 체류시간)이 되겠습니다.
        # 결국 총 체류시간을 tot_t라는 변수에 저장해둔 것입니다.
        tot_t=sum(list(map(lambda x: int(x.split(':')[0])*60+int(x.split(':')[1]),parking_dict[i][1::2])))-sum(list(map(lambda x: int(x.split(':')[0])*60+int(x.split(':')[1]),parking_dict[i][0::2])))
        
        # fees는 다음 정보를 순서대로 보유하고있습니다. [기본시간, 기본요금, 단위시간, 단위요금]
        # 만약 차량 체류시간이 기본시간보다 작다면 기본요금만을 지불하면 됩니다.
        if tot_t<=fees[0]:
            answer.append(fees[1])
        # 그렇지 않을경우 기본요금에 추가로 초과되는 시간을 단위시간으로 나누어주고 그 값의 올림값만큼 단위요금을 곱해준 액수를 지불하면 됩니다.
        else:
            answer.append(fees[1]+math.ceil((tot_t-fees[0])/fees[2])*fees[3])
    return answer

    # tot_t를 구하는 과정이 제 코딩스타일대로 진행하다보니 많이 지저분해졌습니다.
    # 만약 for문을 이용하여 구현한다면 다음과 같을것입니다.

    # tot_t=0
    # for j in range(len(parking_dict[i])):
    #     time=parking_dict[i][j].split(':')
    #     if j%2==1:
    #         tot_t -= int(time[0])*60 + int(time[1])
    #     else:
    #         tot_t += int(time[0])*60 + int(time[1])
            
    # 홀수번째로 들어오는 시간은 입차시간, 짝수번째로 들어오는 시간은 출차시간입니다.
    # (총 출차시간) - (총 입차시간) = (총 체류시간)임으로 상위 코드 내 tot_t와 같은 결과를 가져옵니다!
    # 출입시간리스트가 길어질 수록 이중 for문의 특성상 시간복잡도가 증가합니다. 이를 피하기 위해서 map함수를 이용했습니다..!