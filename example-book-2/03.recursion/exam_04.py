# 호텔 방 배정 (level4)

# "스노우타운"에서 호텔을 운영하고 있는 "스카피"는 호텔에 투숙하려는 고객들에게 방을 배정하려 합니다. 호텔에는 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다. 처음에는 모든 방이 비어 있으며 "스카피"는 다음과 같은 규칙에 따라 고객에게 방을 배정하려고 합니다.

# 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
# ...

# 전체 방 개수 k와 고객들이 원하는 방 번호가 순서대로 들어있는 배열 room_number가 매개변수로 주어질 때, 각 고객에게 배정되는 방 번호를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 최종코드
import sys
sys.setrecursionlimit(1000000)

def find(room,d):
    if room not in d:
        d[room] = room+1
        return room

    nxt = find(d[room]+1,d)
    d[room] = nxt+1
    return nxt
    
def solution(k, rooms):
    full = []
    d = {}

    for room in rooms:
        full.append(find(room, d))
            
    return full






# 처음코드들
def solution(k, room_number):
    full = []
    for req in room_number:
        if req not in full:
            full.append(req)
        else: # 원하는 방이 비어있지 않은 경우
            nxt = req+1
            while True:
                if nxt not in full:
                    full.append(nxt)
                    break
                nxt+=1
                
    return full


    
def solution(k, room_number):
    full = []
    d = {} # n번방을 찾는 사람이 배정받은 마지막 방번호
    for req in room_number:
        if req not in full:
            full.append(req)
            d[req] = req
        else: # 원하는 방이 비어있지 않은 경우
            nxt = req+1
            if req in d:
                nxt = d[req]+1
            while True:
                if nxt not in full:
                    full.append(nxt)
                    d[req] = nxt 
                    if req not in d:
                        for i in range(req,nxt+1):
                            d[i] = nxt
                    break
                nxt+=1
                
    return full

# 접근법
# 처음 풀이는 정석적으로 완전탐색 느낌으로 풀었다.
# 요청받은 순서대로 돌면서 배정되지 않았으면 결과리스트에 넣고
# 이미 배정된 방(=결과리스트에 있는 방)이면 다음 빈방이 나올때까지 while을 돌면서 방넘버를 +1로 확인
# 정확성 테스트는 맞췄지만 효율성이 틀렸다.
# 이유는 두가지였는데, 하나는 다음 빈방이 나올때까지 while을 도는게 요청리스트가 길수록, 중복된 요청이 많을수록 비효율적이어지는것.
# 그리고 이건 마지막에 알게된건데 결과리스트에 있는지를 매번 확인하는 것도 리스트가 클수록 비효율적이었다.

# 그래서 이를 효율적으로 바꾸기 위해서 다음으로 생각한 것이
# 요청을 받고 배정하면서 그 번호가 바로 다음 방을 가리키도록 딕셔너리에 저장하는 것이었다.
# while로 다음 번호를 탐색하는 복잡한 과정을 줄일 수 있고 딕셔너리에 저장함으로써 조회 시간도 줄이는 것을 의도했다.
# 결과적으로 이 접근은 괜찮았다.
# 하지만 구현하는데 있어서 난항을 겪음
# 왜냐하면, 
# 예를들어 [1,1,1,1,2,3] 을 요청했다고 가정해보자. 그리고 n번 방이 가리키는 다음 방 번호를 딕셔너리 d에 저장할 때
# 처음 1을 배정하면 d={1:2}, 두번째 1부터 4번째 1까지 모두 저장하면 순서대로 1,2,3,4 번방을 배정받을 것이고 d = {1:5}가 되어있을것이다.
# 1번방을 호출한다면 5부터 찾으면 되는건 맞지만, 2를 호출했을 때는 또다시 +1시켜가면서 다음 방을 찾아야 한다는 것이 문제였다. 
# 그럼 while이랑 다를 게 없다고 생각했고 그부분에서 막혀서 시간을 오래 썼다.

# 결과적으로, 재귀를 사용하는 데에 익숙하지 않아서 구현을 못한 부분도 큰 것 같다!

