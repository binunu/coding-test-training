# 카드 뭉치
# 코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.

# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
# 한 번 사용한 카드는 다시 사용할 수 없습니다.
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

# 예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 
# 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 
# ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 
# 첫 번째 카드 뭉치에서 "i"를 사용한 후 
# 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 
# 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.

# 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, 
# cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 
# 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.

def solution(cards1, cards2, goal):
    for g in goal :
        if cards1 and g == cards1[0] :
            temp = cards1.pop(0)
            continue
        elif cards2 and g == cards2[0] : 
            temp = cards2.pop(0)
            continue
        else :
            return 'No'
        
    return 'Yes'

# 풀이과정
# goal의 단어를 순회하며 cards1과 cards2의 첫번째 단어와 비교해서
# 같다면 pop(0)으로 해당 단어를 제거하고 다음 단어로 넘어감
# 만약 둘 다 첫번째 단어와 같지 않다면 'No' 반환
# 마지막까지 순회했다면 'Yes' 반환

# 리팩토링
# 리스트를 queue처럼 사용하면 비효율적이다. 
# 왜냐하면 리스트에서 맨 앞에껄 제거하면 그 뒤의 요소를 하나씩 앞으로 당겨오기 때문이다.
# 따라서 인덱스를 사용해 접근하는 방법으로 변경하던지
# collections.deque를 사용해 popleft()메서드로 맨 앞의 요소를 제거하는 방법이 있다.

from collections import deque

def solution(cards1, cards2, goal):
    dq1,dq2  = deque(cards1), deque(cards2)
    for g in goal :
        if dq1 and g == dq1[0] :
            dq1.popleft()
            continue
        elif dq2 and g == dq2[0] : 
            dq2.popleft()
            continue
        else :
            return 'No'
        
    return 'Yes'