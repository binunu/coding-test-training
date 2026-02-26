# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.


def solution(score):
    d = {}
    for i, (eng, math) in enumerate(score):
        if (eng+math)/2 in d.keys():
            d[(eng+math)/2].append(i) 
        else:
            d[(eng+math)/2] = [i] 
    
    arr = sorted(d.items(), key=lambda x: x[0], reverse=True)
    answer = [0] * len(score)
    rank = 1
    for i, pp in enumerate(arr):
        for j in pp[1]:
            answer[j] = rank
        rank += len(pp[1])
    return answer
        

# 풀이과정
# 점수를 평균내어 순서대로 정렬하는 건 쉽다.
# 그러나 기존에 입력받았던 순서대로 등수를 매기는 것에서 어려움이 있었다.
# 딕셔너리를 써서 처음 입력받은 인덱스를 저장한다는 아이디어를 떠올렸다.
# {인덱스 : 평균} 으로 저장하니 나중에 등수를 매길 때 원본배열과 answer배열을 매치시켜서 입력하는 것에 어려움이 있었다.
# 왜냐하면 등수를 매기는 기준 때문인데, 
# 예를 들어 1등이 3명이면 그 다음 학생은 2등이 아닌 4등을 받게 된다.
# 이 계산이 어려워서 다른 방법을 선택했음
# {평균 : [인덱스1, 인덱스2,...]} 의 방식을 선택해서 
# 이전 학생들의 명수를 해당 배열의 길이로 파악할 수 있도록 하였음


# 개선)
# 그러나 다른 풀이방법을 찾아보고 내가 너무 어렵게 풀었다는 사실을 깨달았다.
# 기본 내장 함수인 index()를 써서 아주 간단하게 풀 수 있었다.

def solution(score):
    answer = []
    top_s = sorted([sum(s) for s in score],reverse=True) 
    print(top_s)
    
    return [top_s.index(sum(s))+1 for s in score]