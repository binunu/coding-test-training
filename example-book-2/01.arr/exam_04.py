# 거리두기 (level 2)
# 개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

# 코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
# 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

# 1.대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 2.거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
# 3.단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

# 5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 
# 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
def check(place,p):
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            x1 = p[i][0]
            x2 = p[j][0]
            y1 = p[i][1]
            y2 = p[j][1]

            if abs(x1-x2)+abs(y1-y2) == 1:
                return 0
            if abs(x1-x2)+abs(y1-y2) == 2:
                #같은행
                if x1==x2:
                    if place[x1][(y1+y2)//2] != 'X':
                        return 0
                #같은열
                elif y1==y2:
                    if place[(x1+x2)//2][y1] != 'X':
                        return 0
                #대각선
                else:
                    if place[x1][y2] != 'X' or place[x2][y1] != 'X':
                        return 0
                
    return 1

def solution(places):
    answer = []
    # p를 찾은 다음 p의 옆, 아래쪽으로의 맨헤튼거리 내를 확인하고 
    # 그 안에 p와의 사이에 파티션이 없는 사람이 있으면 0을 리턴. 
    for place in places:
        p = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p.append([i,j])
        answer.append(check(place,p))
                
    return answer

# 풀이과정
# 완전탐색을 사용했는데, 
# 대각선에 p가 있을 때 그 사이를 확인하는 방법을 어떻게 구현해야 할 지 막막했다.
# 이 부분을 검색하여 찾아보았고,
# 맨헤튼거리가 2일때 x좌표와 y좌표가 다르면 대각선에 위치한다는 점을 이용해서 풀 수 있었다.