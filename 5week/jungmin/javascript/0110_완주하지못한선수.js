function solution(participant, completion) {
    const arr = [...participant, ...completion].sort();
    for(i=0; i<arr.length; i++){
        if(arr[2*i] != arr[2*i+1]){
            return arr[2*i];
        }
    }
    return arr[arr.length-1];
}