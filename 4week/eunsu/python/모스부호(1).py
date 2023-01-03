def solution(letter):
    answer = ''
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    for char in letter.split(' '):
        # 딕셔너리 활용 -> dict[key] = value
        answer += morse[char]   
    return answer

# letter1 = ".... . .-.. .-.. ---"
# print(solution(letter1))    -> hello