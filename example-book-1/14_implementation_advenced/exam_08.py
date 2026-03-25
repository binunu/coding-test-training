# 대충 만든 자판 (level 1)
# 휴대폰의 자판은 컴퓨터 키보드 자판과는 다르게 하나의 키에 여러 개의 문자가 할당될 수 있습니다. 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.

# 예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.

# 같은 규칙을 적용해 아무렇게나 만든 휴대폰 자판이 있습니다. 이 휴대폰 자판은 키의 개수가 1개부터 최대 100개까지 있을 수 있으며, 특정 키를 눌렀을 때 입력되는 문자들도 무작위로 배열되어 있습니다. 또, 같은 문자가 자판 전체에 여러 번 할당된 경우도 있고, 키 하나에 같은 문자가 여러 번 할당된 경우도 있습니다. 심지어 아예 할당되지 않은 경우도 있습니다. 따라서 몇몇 문자열은 작성할 수 없을 수도 있습니다.

# 이 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.

# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수를 완성해 주세요.

# 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.

def solution(keymap, targets):
    answer = []
    for tg in targets:
        cnt=0
        for x in tg:
            if cnt==-1:break
            min_idx=101
            for key in keymap:
                idx = key.find(x)
                if idx!=-1:
                    min_idx = min(min_idx,key.find(x)) 
            if min_idx == 101:
                cnt = -1
                break
            cnt+=min_idx+1 # 한 알파벳을 누르는 횟수
        
        answer.append(cnt)
    return answer

# 개선 1)
# 매 target을 모두 돌면서 확인하면 keymap과 target의 길이가 길어질수록 효율성이 떨어짐.
# dict를 활용해서 가장 작은 횟수를 저장해둔다음 한번에 계산하도록 고침
def solution(keymap, targets):
    answer = []
    min_idx = {} 
    # 알파벳별 최소숫자를 저장
    for tg in targets:
        for x in set(tg):   
            idx=101
            for key in keymap:
                if key.find(x) != -1:
                    idx = min(idx, key.find(x)+1) 
            min_idx[x] = idx   
    # 계산
    for tg in targets:
        cnt = 0
        for x in tg:
            if min_idx[x] == 101:
                cnt = -1
                break
            else:
                cnt+=min_idx[x]
        answer.append(cnt)
    return answer


# 개선2)
# 위코드는 모든 target에 대해 다 검사한다. 만약 'aaab', 'aaac'와같은 targets가있으면
# a,b,a,c < 이렇게 계산을 할 것이다
# 이를 해결하기 위해 keymap을 돌면서 미리 저장을 해 두면 중복을 최소화 할 수 있다.
def solution(keymap, targets):
    answer = []
    min_idx = {} 
    # 알파벳별 최소 숫자 저장2 키맵기준
    for key in keymap:
        for i,x in enumerate(key) : # 어차피 먼저나온게 가장 최소횟수기 때문에 set을 하지 않아도 됨
            if x not in min_idx or i+1 < min_idx[x]:
                min_idx[x] = i+1
    for tg in targets:
        cnt = 0
        for x in tg:
            if x not in min_idx:
                cnt = -1
                break
            else:
                cnt+=min_idx[x]
        answer.append(cnt)
    return answer