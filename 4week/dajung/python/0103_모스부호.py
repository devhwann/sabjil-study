#프로그래머스 level 0
#https://school.programmers.co.kr/learn/courses/30/lessons/120838

#길이가 1이상 1000이하인 문자열 letter 
def solution(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }  
    splited = letter.split(" ")
    decryption = ""
    for i in splited:
        decryption += morse[i]
    return decryption
