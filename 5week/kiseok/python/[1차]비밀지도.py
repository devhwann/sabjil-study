def solution(n, arr1, arr2):
    # map1과 map2를 만듭니다.
    # format(n,'b')를 이용하면 n을 이진수로 표현할 수 있습니다.
    # n.zfill(x)는 n을 x의 자리수 만큼 맞춰줍니다.
    # ex) 48.zfill(3) => 048의 형태로 반환해줍니다.
    # list(map(str,x))는 x를 문자열로 mapping해주며 이를 다시 리스트로 반환하는 형태입니다.
    # 리스트 내 for 문을 인라인으로 정의하여 이중리스트인 arr의 내부 리스트를 한줄씩 순서대로 반환하여 다시 이중 리스트를 만들어줍니다.  
    map1=[list(map(str,format(i,'b').zfill(n))) for i in arr1]
    map2=[list(map(str,format(i,'b').zfill(n))) for i in arr2]

    # tmp는 map1과 map2를 취합한 단일리스트입니다.
    # tmp의 경우 if문과 for문을 인라인으로 정의한 리스트입니다.
    # tmp는 이중for문을 이용하여 map1과 map2내 각각의 요소를 가져와 각 조건에 맞는 결과를 반환합니다.
    # 만약 map1과 map2 각각의 요소가 0이라면 해당 위치는 길 (" ") 로 정의할 수 있고 이외의 경우는 벽("#")으로 정의할 수 있습니다.
    # 결과적으로 tmp는 각 요소의 조건에 따라 지도의 정보를 단일리스트로 저장하고 있습니다.
    tmp = [' ' if map1[i][j]=='0' and map2[i][j]=='0' else '#' for i in range(n) for j in range(n)]

    # return되는 answer는 요소가 각 행의 지도정보를 포함해야 합니다.
    # "".join(list)는 각 리스트 요소를 하나의 문자열로 반환해주는 함수입니다.
    # 인라인 for문을 이용해 tmp를 n단위로 slicing하여 문자열을 만들어 반환해줍니다.
    return ["".join(tmp[n*i:n*(i+1)]) for i in range(n)]

    #부족한 부분이 많고 비효율적일 수 있습니다.. 효율적인 코드나 팁이 있다면 알려주시면 감사하겠습니다... (_ _)
