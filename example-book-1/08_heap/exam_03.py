# 회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다.
# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. 
# Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
# Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,
# 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

import heapq
def solution(n, works):
    answer = 0
    wk = []
    for w in works:
        heapq.heappush(wk, -w)
    
    #퇴근까지 일 하기
    #근데 피로도를 낮추려면 야근시점에 각 일의 숫자가 골고루 작아야함 -> 양이 많은 일부터 처리
    for _ in range(n):
        if wk[0] == 0: break
        top = heapq.heappop(wk)
        heapq.heappush(wk, top+1)
        
    #퇴근이후 피로도 계산
    for w in wk:
        answer += (-1 * w) * (-1 * w)
        
    return answer