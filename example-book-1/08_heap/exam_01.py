# "명예의 전당"이라는 TV 프로그램에서는 매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다. 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다. 즉 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다. k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.

# 이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표합니다. 예를 들어, k = 3이고, 7일 동안 진행된 가수의 점수가 [10, 100, 20, 150, 1, 100, 200]이라면, 명예의 전당에서 발표된 점수는 아래의 그림과 같이 [10, 10, 10, 20, 20, 100, 100]입니다.
# 명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때, 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.

#최종코드
import heapq
def solution(k, score):
    answer = []
    r = []
    for i,s in enumerate(score):
        if i < k:
            heapq.heappush(r,s)

        else:
            if r[0] < s: # 명전갱신
                heapq.heappop(r)
                heapq.heappush(r,s)

        answer.append(r[0])
    return answer


#원래코드
import heapq
def solution(k, score):
    answer = []
    rank = []
    for i,s in enumerate(score):
        if i < k:
            heapq.heappush(rank,s)
            top = heapq.heappop(rank)
            answer.append(top)
            heapq.heappush(rank,top)
            
        else:
            score = heapq.heappop(rank)
            if s > score: # 명전 밀어내기. 다음 스코어 뽑기
                top = heapq.heappushpop(rank,s)
                answer.append(top)
                heapq.heappush(rank,top)
            else: # 명전 유지
                answer.append(score)
                heapq.heappush(rank,score)
           
    return answer



# 풀이과정
# k일 전에는 최하위 점수(이하 루트)를 꺼내고 다시 넣음(모두 명전에 오르기 때문에 다시 넣어줘야 함)
# k일 후에는 일단 루트를 꺼낸다음에 새로운 점수(s)와 비교
#     만약 루트 > s 이면 (명예의전당 갱신)
#         s를 명예의 전당에 넣음
#         그리고 새로운 루트를 추출 후 answer에 넣고 다시 명예의 전당에 넣음
#     만약 루트 < s 이면 (명예의 전당 변동 x)
#         루트를 answer에 넣고 다시 명예의 전당에 넣음

# 같은동작인데, 간과하고 있던 부분은
# heap이 특별한 자료구조가 아닌 배열로 이루어졌다는 점이다.
# 굳이 확인을 위해 pop-push를 할 필요 없고 그냥 rank[0] 으로 배열처럼 확인을 하면 되는것이었음. 
# 그리고 매번 answer에 넣는 과정은 마지막에 한번만 하도록 바꾸니 코드가 훨씬 간결해 졌다.