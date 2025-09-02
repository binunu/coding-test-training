# 옹알이(2)
# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 
# 연속해서 같은 발음을 하는 것을 어려워합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(babbling):
    answer = 0
    word = ['aya','ye','woo','ma']
    pre = ''
    for b in babbling:
        for w in word :
            if b.find(w+w) >= 0 : 
                continue
            b = b.replace(w, " ")
        
        if b.strip() == '' :
            answer+=1
                
    return answer

# 풀이과정
# 각 단어에 대해 같은 발음이 연속해서 나오는지 (w+w)로 확인하고
# 이전 옹알이(1)과 같이 w를 공백으로 치환
# 공백을 제거했을 때 빈 문자열이면 옹알이 가능한 단어이므로 answer 증가
