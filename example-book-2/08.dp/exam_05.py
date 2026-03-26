# 도둑질 level4
# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

# image.png

# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

def solution(money):
    mn0 = money[:]
    mn1 = money[:]
    # 한칸건너씩 계속 털어야함. 
    # 모든집이 연결되어있기 때문에 마지막집은 첫집을 안털었으면 털수잇고 첫집을 털었으면 못텀
    # -> 두 가지로 경우를 나눠서 계산
    # 1부터 각 index에 i번째에서 가질 수 있는 최대값을 저장(i집을 털든 안털든 관계x)
    # i-1번째꺼랑 i-2+자기꺼를 비교해서 큰 걸 저장
    mn0[1] = money[0] # 첫집털기
    mn1[2] = max(mn1[1],mn1[2])#첫집안털기
    
    for i in range(2,len(money)):
        mn0[i] = max(mn0[i-2]+mn0[i], mn0[i-1]) 
    for i in range(3,len(money)):
        mn1[i] = max(mn1[i-2]+mn1[i], mn1[i-1]) 
        
    return max(mn0[-2],mn1[-1])
