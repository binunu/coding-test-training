# 디스크 컨트롤러 level 3
# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 이 문제에서는 우선순위 디스크 컨트롤러라는 가상의 장치를 이용한다고 가정합니다. 우선순위 디스크 컨트롤러는 다음과 같이 동작합니다.
# ...
# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 정수 배열 jobs가 매개변수로 주어질 때, 우선순위 디스크 컨트롤러가 이 작업을 처리했을 때 모든 요청 작업의 반환 시간의 평균의 정수부분을 return 하는 solution 함수를 작성해 주세요.

import heapq
def solution(jobs): # 
    answer = 0
    arr=[(s,t,i) for i, (s,t) in enumerate(jobs)]    
    arr.sort()
    time = 0
    q=[]
    while arr or q: 
        while arr and arr[0][0] <= time:
            (s,t,i) = arr.pop(0)
            heapq.heappush(q,(t,s,i))
        if q:
            (t,s,i) = heapq.heappop(q)
            time += t
            answer+=time-s #처리완료시간-요청시간
        else:
            time+=1
                
    return answer//len(jobs)
         