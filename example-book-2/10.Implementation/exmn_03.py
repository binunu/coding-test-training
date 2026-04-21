# 스킬 트리 level2
def solution(skill, skill_trees):
    answer = 0
    d = {}
    for i in range(len(skill)-1):
        d[skill[i+1]] = skill[i]
    
    for stree in skill_trees:
        ok = ''
        for s in stree:
            key = s
            flag = True
            while key in d:
                if d[key] not in ok: # 
                    flag = False
                    break
                key = d[key]
            if flag:
                ok+=s
            else:
                break
        if ok == stree:
            answer+=1

    return answer

# 첫 풀이과정
# 그냥 문제에서 제시한 조건을 따라가며 구현했다.
# 딕셔너리로 각 스킬의 선행스킬을 저장한 후, 
# 제시된 스킬트리를 돌며 선행스킬이 있으면 계속 타고타고 탐색하여 모두 있는지 찾는 방식이다.
# 문제는 맞췄지만, 타고타고 하는 과정을 좀 더 효율적으로 바꿀 수 있는 방법을 찾아보았다.

# 개선 1. 인덱스로 다음 배울 스킬을 저장.
# 만약, 스킬순서가 ABC라면,  A를 무조건 먼저 배워야 하므로 배워야 할 스킬 인덱스에 0을 저장.
# 스킬트리를 돌며 A를 배웠다면 B의 인덱스를 저장하는 방식으로 간단히 관리할 수 있다.
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        idx = 0
        isok = True
        for s in tree:
            if s in skill: # 스킬순서가 있는 스킬이라면
                if skill[idx]!=s:
                    isok = False
                    break
                idx+=1
        if isok:
            answer+=1
    return answer

# 개선 2. 애초에 스킬순서에 있는 스킬만 뽑아서 더 간결하게 확인할 수도 있다.
# 스킬트리를 돌며 스킬순서에 있는 스킬만 추출해 새 문자열로 만든다.
# 스킬순서 문자열이 방금 만든 새 문자열로 시작하는지 여부만 파악하면 끝이다.(무조건 A부터 시작해야 하므로)
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        st = ''
        for s in tree:
            if s in skill:
                st+=s
        if skill.startswith(st):
            answer+=1
    return answer