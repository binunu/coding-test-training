# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

import heapq
def solution(sc, k):
    answer = 0
    heapq.heapify(sc)
  
    while sc[0] < k :
        if len(sc) < 2 : return -1
        
        z = heapq.heappop(sc)
        y = heapq.heappop(sc)
        
        heapq.heappush(sc,z + (y*2))
        answer+=1
        
    return answer

# 풀이과정
# 섞을 수가 없는 상태 == 원소가 1개밖에 안남았을 때
# 그 전까지는 heap에서 2개를 꺼내서 섞고 다시 넣는 과정 반복
# 헷갈린 점은 꺼낸 원소가 k보다 커도 섞을 수 있다는 것임(지문에 k미만이어야 섞을 수 있다고 하지 않았기 때문에)
