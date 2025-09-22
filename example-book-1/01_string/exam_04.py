# 숨어있는 숫자의 덧셈(2)
# 문자열 my_string이 매개변수로 주어집니다.
# my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = 0
    pre=''
    isNoNum = True
    for c in my_string:
        if(c.isdecimal()):
            isNoNum = False
            if pre:
                pre=pre+c
            else:
                pre=c
        else:
            answer+=int(pre or 0) 
            pre=''
    answer += int(pre or 0)
    return answer if not isNoNum else 0

# 풀이전략
# 문자열을 순회하며 숫자인지 아닌지 판단
# 숫자일 경우, 이전에 숫자가 있었는지 판단해 이어붙이기
# 숫자가 아닐 경우, 이전에 숫자가 있었다면 answer에 더하기
# 마지막에 남아있는 숫자도 더하기
# 만약 문자열에 숫자가 하나도 없을 경우 0을 반환


# 리팩토링
def solution(my_string):
    answer = 0
    pre=''
    for c in my_string:
        if(c.isdecimal()):
            pre+=c
        else:
            answer+=int(pre or 0) 
            pre=''
    return answer + int(pre or 0)

# 1. 이전의 pre가 있었는지 여부는 상관없음. 왜냐하면 있든 없든 pre에 c를 이어붙이기 때문
# isNoNum 변수를 제거 하고, 마지막에 answer를 반환할 때
# 2. 숫자가 없었는지 판단하는 isNoNum변수도 불필요
# 어차피 숫자가 없다면 결국 answer은 0이 되기 때문
# 그리고 자연수밖에 없기 때문에 숫자가 있는데 0이 될 가능성도 없다.(음수가 없어서)