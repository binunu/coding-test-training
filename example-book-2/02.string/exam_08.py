# 신규 아이디 추천 (level 1)
# 카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다.
#  "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
# 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for s in new_id:
        if not s.isdigit() and not s.isalpha() and s not in ('-','_','.'):
            new_id = new_id.replace(s,"")

    while new_id.find('..') > -1:
        new_id = new_id.replace("..",".")
    
    if new_id.startswith('.'):
        new_id = new_id[1:]
        
    if new_id.endswith('.'):
        new_id = new_id[:-1]
        
    if new_id == '':
        new_id = 'a'
        
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
        
    if len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))
        
    return new_id