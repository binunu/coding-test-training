# 소수 찾기 – Level 2
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
from itertools import product
    
def solution(user_id, banned_id):
    res = [[] for _ in range(len(banned_id))]
    for i,bid in enumerate(banned_id):
        for uid in user_id:
            if len(bid) == len(uid): # zip은 개수가 같은 짝이 없으면 안나옴
                check=True
                for b,u in zip(bid,uid):
                    if b!=u and b != '*':
                        check=False
                if check:
                    res[i].append(uid)
                    
    answer=set()
    for p in product(*res):
        if len(set(p)) == len(banned_id):
            answer.add(tuple(sorted(p)))

    return len(answer)