# 마지막앨범 level 3
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

from collections import defaultdict
def solution(genres, plays):
    answer = []
    d=defaultdict(list)
    # {장르: [재생횟수, 고유번호]...} 로 저장
    i=0
    for g,p in zip(genres, plays):
        d[g].append([i,p])
        i+=1
    # 장르안에서 플레이순 정렬

    arr=sorted(d.items(),key=lambda x:-sum(play for _,play in x[1]))
    for g, s in arr:
        s.sort(key=lambda x : (-x[1],x[0]))
        for i in s[:2]:
            answer.append(i[0])
    return answer