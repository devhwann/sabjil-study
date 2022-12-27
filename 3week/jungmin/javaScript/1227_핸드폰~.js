function solution(phone_number) {
    var star = ""
    for(var i=0; i<phone_number.length-4; i++){
        star += "*"
    }
    var last4 = phone_number.substr(phone_number.length-4, 4);
    return star + last4;
}

// 끝 네 자리를 제외한 나머지 숫자를 *로 바꾸고, 끝 네자리와 합쳐주었습니다.