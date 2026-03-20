# 호텔 방 배정 (level4)

# "스노우타운"에서 호텔을 운영하고 있는 "스카피"는 호텔에 투숙하려는 고객들에게 방을 배정하려 합니다. 호텔에는 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다. 처음에는 모든 방이 비어 있으며 "스카피"는 다음과 같은 규칙에 따라 고객에게 방을 배정하려고 합니다.

# 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
# ...

# 전체 방 개수 k와 고객들이 원하는 방 번호가 순서대로 들어있는 배열 room_number가 매개변수로 주어질 때, 각 고객에게 배정되는 방 번호를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

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

