# 문자열 계산하기
# my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
# 문자열 my_string이 매개변수로 주어질 때,
# 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

# 전략
# 각 숫자를 분리한 후 배열에 넣어 합계로 계산하는 방식을 떠올림
# 입출력 예를 보고 한자리 숫자로만 생각해서
# 단순히 공백을 제거한 문자열을 붙인 후 홀수 번째 자리가 연산자라고 생각했음
# 하지만 숫자의 자리수가 커질 때, 이 조건은 오류가 있음
# 그래서 공백을 기준으로 숫자를 자른 후 배열에 넣는 것으로 수정

# 풀이과정 1
# "1", "+", "2" 와 같이 연산자와 숫자를 모두 분리시켜 연산자가 -일 때, 뒤의 숫자에 -1을 곱해서 배열에 넣는 방식
# 이후 마지막에 sum()으로 합계를 구함
def solution(my_string): 
    text = my_string.split(" ")
    arr = [int(text[0])]
    for i in range(1, len(text), 2):
        if text[i] == '-':
            arr.append(-1 * int(text[i+1]))
        else:
            arr.append(int(text[i+1]))
        
    return sum(arr)


# 풀이과정 2
# tip:"+2", "-3" 와 같이 연산자와 숫자가 합쳐진 문자열을 int()로 변환할 수 있다.

def solution(my_string): 
    text = my_string.split(" ")
    sum = int(text[0])
    for i in range(1, len(text)-1,2):
        sum += int(text[i]+text[i+1])
    return sum

# 풀이과정 3
# 이 모든걸 한줄로도 가능
# eval() 함수를 사용하면 문자열로 된 수식을 계산할 수 있음(공백도 상관없음)
# 하지만 eval() 함수는 보안에 취약할 수 있어 실제 서비스에서는 사용하지 않는 것이 좋음
def solution(my_string):
    return eval(my_string)
