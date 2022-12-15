function solution(sides) {
    if (sides[0]+sides[1] <= sides[2] || sides[0]+sides[2] <= sides[1]|| sides[1]+sides[2] <= sides[0]) return 2;
    else return 1;
}
