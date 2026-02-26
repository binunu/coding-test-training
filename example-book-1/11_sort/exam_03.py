# 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

from collections import Counter
def solution(before, after):
    a = Counter(after)
    b = Counter(before)
    return 1 if a==b else 0


# 간단하게 바로 풀었음