# 바탕화면 정리

def solution(wallpaper):
    answer = []
    xpos = (50,0)
    ypos = (50,0)
    # 가장 왼쪽, 가장 오른쪽, 가장 위, 가장 아래의 x, y 좌표를 갱신
    for i, wall in enumerate(wallpaper):
        for j, w in enumerate(wall):
            if w == '#':
                xpos = (min(xpos[0], i), max(xpos[1], i+1))
                ypos = (min(ypos[0], j), max(ypos[1], j+1))
    
    return [xpos[0],ypos[0], xpos[1], ypos[1]]


# 주의
# 오른쪽, 아래 좌표는 +1을 해야함!