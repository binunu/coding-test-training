# 인덱스 바꾸기
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string, num1, num2):
    arr = list(my_string)
    s1 = arr[num1]
    s2 = arr[num2]
    arr[num2] = s1
    arr[num1] = s2
    return ''.join(arr)

# 풀이과정
# 문자열은 변경할 수 없으므로 리스트로 변환
# num1, num2에 해당하는 문자를 서로 바꿈
# 리스트를 다시 문자열로 변환해 반환

# 리팩토링
def solution(my_string, num1, num2):
    arr = list(my_string)
    arr[num1], arr[num2] = arr[num2], arr[num1]
    return ''.join(arr)
