# 보석 쇼핑 level 3
# ...
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

# 처음풀이
# def solution(gems):
#     answer = []
#     s = 1
#     e = 100000
#     tgcnt = len(set(gems))
#     while s<=e: 
#         mid = (s+e)//2
#         isfind=False
#         for i in range(len(gems)):
#             if len(set(gems[i:i+mid])) == tgcnt:
#                 isfind=True
#                 break
#         print("for결과:",isfind)
#         if isfind:
#             e = mid-1
#             answer = [i+1,i+mid]
#         else:
#             s = mid+1
#     return answer

# 처음 풀이는 이진탐색을 생각햇다. 
# 어떤 구간을 타겟으로 설정하고 그 구간만큼 돌며 조건을 만족하는지 확인 후 범위를 좁혀나갓다.
# 정확도는 만족햇지만 시간초과가 났음
# 아마도 이유는 조건을 확인하는 for- 구문에서 발생한 것 같다. 
# 일일이 확인하며 set()과 len()을 반복하는것에서 시간초과가 나지 않았을까 생각했다.

# 아래는 그를 해결하고자 슬라이딩 윈도우(투포인트알고리즘)를 사용한 풀이이다.
# 그리고 매번 len(set())를 사용해 검사하면 비효율적이므로 이를 hash를 사용해서 길이를 비교하도록 했다. 
# 최종코드
from collections import defaultdict
def solution(gems):
    n = len(gems)
    tg = len(set(gems))
    answer = [1,n] # 최대값으로 설정하고 조건을 만족하면 갱신(최소값찾기)
    d = defaultdict(int)
    start=0
    end=0
    while end < n:
        #타겟조건을 만족하지 않으면 계속 추가
        d[gems[end]]+=1
        
        #타겟조건을 만족하면 정답 갱신
        while len(d)==tg:
            if end-start < answer[1]-answer[0]:
                answer = [start+1,end+1]
            d[gems[start]] -=1
            if d[gems[start]] == 0:
                del d[gems[start]]
            start+=1
            
        end+=1
    return answer
