# 평행 (level 0)
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def solution(dots):
    case = [[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
    
    for pos1,pos2 in case:
        ax1= dots[pos1[0]][0]
        ay1= dots[pos1[0]][1]
        ax2= dots[pos1[1]][0]
        ay2= dots[pos1[1]][1]
        
        bx1= dots[pos2[0]][0]
        by1= dots[pos2[0]][1]
        bx2= dots[pos2[1]][0]
        by2= dots[pos2[1]][1]
        
        gi_a = (ay2-ay1)/(ax2-ax1)
        gi_b = (by2-by1)/(bx2-bx1)
        
        if gi_a==gi_b:
            return 1
        
    return 0

# 점 네개로 만들 수 있는 모든 조합이 아닌
# 점 네개를 두개 두개 짝지어야함.
