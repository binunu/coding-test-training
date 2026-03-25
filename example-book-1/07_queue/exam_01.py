# 문제 설명
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
from collections import deque
def solution(numbers, direction):
    dq = deque(numbers)
    if direction == 'left':
        dq.rotate(-1)
    else:
        dq.rotate(1)
    return list(dq)

# 풀이과정
# deque의 rotate 메서드를 사용하여 간단히 구현