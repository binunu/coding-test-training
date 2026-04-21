# 줄 서는 방법 level 2


# 시간초과
# from itertools import permutations
# def solution(n, k):
#     pl = list(permutations([i for i in range(1,n+1)],n))
#     return pl[k-1]

import math
def solution(n, k):
    answer = []
    arr = [i for i in range(1,n+1)]
    k -= 1
    while n > 0:
        n-=1
        fn = math.factorial(n)
        answer.append(arr[k//fn])
        arr.remove(arr[k//fn])
        k %= fn
    return answer


# 첫 자리고정, 다음자리부터 경우의수 (n-1)!
# 첫자리를 알아내는법 : 내가 속한 첫번째블럭 - (n-1) 값을 (k-1)로 나누어서 몫으로 알 수 있음
# (0 base로 계산하기위해 k-1)
# 새로 블록 안에서의 자리찾기 : 나머지 이용
    
