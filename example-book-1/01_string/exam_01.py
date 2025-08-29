# 옹알이(1)
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(babbling):
    answer = 0
    word = ['aya', 'ye', 'woo', 'ma']
    for b in babbling:
        for w in word:
            b=b.replace(w,' ',1)
        if(b.strip()=='') :
            answer+=1
    return answer

# 풀이전략
# 처음에 replace(w,'')를 사용해서 해당 문자열을 공백으로 치환하려고 시도.
# 그러나 예를 들어, 'yayae' 와 같은 문자열일 경우 발음할 수 없는 단어임에도
# 중간의 'aya' 가 사라지고 앞의 'ye'가 남아 발음할 수 있는 단어로 잘못 인식되는 문제가 발생.
# 따라서 replace(w,' ',1)로 바꿔서 한 번에 하나의 문자열만 공백으로 치환하도록 변경.
# 그리고 나서 b.strip()을 사용해서 공백을 제거한 후, 빈 문자열인지 확인.

# tip: s.replace()의 세 번째 인자로 몇 회 치환할지 지정 가능.