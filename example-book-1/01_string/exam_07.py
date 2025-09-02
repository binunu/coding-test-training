# 자릿수 더하기
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

def solution(n):
    return sum(int(i) for i in str(n))

# 풀이과정
# n을 문자열로 변환해 각 자리 숫자를 순회하며 정수로 변환
# 각 자리 숫자를 모두 더해 반환