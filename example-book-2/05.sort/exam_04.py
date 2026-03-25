# 
def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(reverse=True, key=lambda x: x*3)
    return str(int("".join(numbers)))

# 풀이
# 단순히 내림차순만 해서 이어붙이면 안됨
# 3,30과 같이 내림차순과 실제 붙였을 때의 크기가 반대될 수 있음
# 이런 경우까지 고려하기 위해서는 숫자의 최대 크기가 1000까지인 걸 참고해서
# 3 번 이어붙인 문자열을 비교하면 된다. 