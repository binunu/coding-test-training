# 순위 검색
# 리스트를 최소한으로 돌려면..
# 딕셔너리에 [조건] : 점수를 저장
# 예를들면 {python: [50,60,100...]}
# 그 후
from bisect import bisect_left
from itertools import combinations #리스트중에 2개씩 뽑아서 조합
from collections import defaultdict
def solution(info, query):
    answer = []
    d=defaultdict(list)
    for item in info:
        tmp=item.split()
        condition=tmp[:-1]
        score=int(tmp[-1])
        for n in range(5): # '-'가 들어갈 개수. 0개부터 4개까지
            for comb in combinations(range(4),n): # '-' 가 들어갈 위치 조합
                keyarr = condition[:]
                for c in comb:
                    keyarr[c] = '-'
                d[''.join(keyarr)].append(score)
    for key in d:
        d[key].sort()
        
    for q in query:
        qarr=q.split()
        qtxt=''
        for x in qarr[:-1]:
            if x != 'and':
                qtxt+=x  
        idx = bisect_left(d[qtxt], int(qarr[-1]))
        answer.append(len(d[qtxt])-idx)
    return answer

#풀이
# 16가지 경우의 수를 dict에 저장해서 
# arr을 계속 돌지 않는게 핵심이었음 

# 아래 코드는 첫 1문제만 맞추고 다틀림.
# def findIdx(score, target, start, end):
#     mid = (start+end)//2
#     if start >= end:
#         return mid
#     if target <= score[mid]:
#         return findIdx(score, target, start, mid-1)
#     else:
#         return findIdx(score, target, mid+1, end)
        
    
# def solution(info, query):
#     answer = []
#     # 개발언어 직군 경력 소울푸드 점수
#     # 점수를 기준으로 오름차순 -> list로 변환
#     arr=[i.split(" ") for i in info]
    
#     arr.sort(key=lambda x : int(x[4]))
#     score= [int(a[-1]) for a in arr]
#     for q in query:
#         qlist = q.split(" and ")
#         tmp = qlist[-1].split(" ")
#         qlist.pop()
#         qlist+=tmp
        
#         target = int(qlist[-1])
#         i = findIdx(score, target, 0, len(score))
#         cnt = 0
#         for a in arr[i:]:
#             isTrue = True
#             for word in qlist:
#                 if word != '-':
#                     if word not in a and not word.isdigit():
#                         isTrue = False
#             if isTrue: cnt+=1
#         answer.append(cnt)
        
#     return answer