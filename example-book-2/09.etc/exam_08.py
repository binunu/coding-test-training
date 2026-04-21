# 가사검색 level 4
# 친구들로부터 천재 프로그래머로 불리는 "프로도"는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다.
# 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.


def insert(trie, word):
    # 새 포인터 생성
    current = trie
    current[len(word)] = current.get(len(word),0)+1
    for w in word:
        if w not in current:
            current[w] = {}
        current = current[w] #이동을 먼저 하고 숫자 기록
        
        if len(word) not in current:
            current[len(word)] = 0
        current[len(word)] +=1 
         # 포인터가 가리키는 노드 이동(깊은 곳으로), 이미있으면 바로이동, 없으면 생성 후 이동
    
    # for가 끝난 후 (마지막저장후) 가리키는 노드에 end를 마크
    current['end'] = True

def search(trie, word, cnt):
    if word == '':
        return trie.get(cnt,0)
    current = trie
    for w in word:
        if w not in current:
            return 0
        current = current[w]
    #for문을 다 돌고 현재 가리키는 노드에 개수 파악
    return current.get(cnt,0) # cnt가 없을 때 에러가 남

def solution(words, queries):
    trie={} # 루트를 가리키는 포인터라고 생각
    reverse_trie={}
    answer = []
    # 트라이에 넣기
    for word in words:
        insert(trie,word)
        insert(reverse_trie, word[::-1]) # ?가 처음에 오는 단어는 뒤집어서 관리
 
    #print(trie)
    # 트라이에서 찾기
    for query in queries:
        if query[0]=='?':
            if query[-1] =='?':
                answer.append(search(trie,'',len(query)))
                continue
            for i,e in enumerate(query):
                if e != '?':    
                    answer.append(search(reverse_trie, query[i:][::-1], len(query)))
                    break
        else:
            idx = query.find('?')
            answer.append(search(trie,query[:idx], len(query)))
                
    return answer
    