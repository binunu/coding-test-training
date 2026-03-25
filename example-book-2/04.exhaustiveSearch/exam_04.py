# 
from itertools import permutations
def calc(num1, num2, oper):
    if oper=='+':
        return num1+num2
    elif oper=='*':
        return num1*num2
    else:
        return num1-num2

def solution(expression):
    elist = []
    opers=set()
    pre=0
    for i,a in enumerate(expression):
        if a in ['+','-','*']:
            elist.append(int(expression[pre:i]))
            elist.append(a)
            opers.add(a)
            pre = i+1
    elist.append(int(expression[pre:]))
    
    opers=list(permutations(opers,len(opers)))
    
    maxv=0
    for oper in opers:
        clist = elist.copy()
        for o in oper:
            while o in clist:
                i=clist.index(o)
                clist[i-1:i+2] = [calc(clist[i-1],clist[i+1],o)]
        maxv=max(abs(clist[0]),maxv)
    return maxv

# 참고사항
# 숫자연산을 eval()로하는것보다 calc()처럼 분기처리하는게 훨씬 연산속도가 빠르다


#from itertools import permutations
# # def order(ops): # 순서 o, 중복 x -> per
# def findidx(text,i): # text 에서 i인덱스 앞뒤의 숫자 끝 인덱스 반환
#     res=[0,len(text)]
#     for s in range(i-1,-1,-1):
#         if text[s] in ['+','-','*']:
#             res[0] = s+1
#             break
#     for e in range(i+1,len(text)):
#         if text[e] in ['+','-','*']:
#             res[1] = e
#             break
#     return res

# def solution(expression):
#     answer = 0
#     # 우선순위구하기
#     ops = []
#     for a in ['+','-','*']:
#         if expression.find(a) > -1:
#             ops.append(a)
#     oplist = list(permutations(ops,len(ops)))
#     # 우선순위별 계산 후 최대값
#     for op in oplist:
#         txt = expression
#         for o in op:
#             while txt.find(o) != -1:
#                 i = txt.find(o)
#                 s, e = findidx(txt,i)
#                 txt = txt[:s] + str(eval(txt[s:e])) + txt[e:]
#         answer = max(answer, abs(int(txt))) 
        