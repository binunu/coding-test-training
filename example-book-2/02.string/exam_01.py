#시저암호
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
def solution(s, n):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for x in s:
        if x == " ":
            answer+=x
        elif x in alpha:
            idx = alpha.find(x) + n
            if idx >= len(alpha):
                idx = (alpha.find(x) + n) % len(alpha)
            answer+=alpha[idx]
        else:
            idx = ALPHA.find(x) + n
            if idx >= len(ALPHA):
                idx = (ALPHA.find(x) + n )% len(ALPHA)
            answer+=ALPHA[idx]
    return answer

# 풀이과정
# ord() 등, 아스키 코드를 만드는 함수가 기억이 안나서 
# 안쓰고 풀었음