class MinHeap:
    def __init__(self):
        self.a = []

    def __len__(self):
        return len(self.a)
    
    def peek(self):
        if not self.a:
            raise IndexError("peek from empty heap")
        return self.a[0]
    
    # 삽입
    def push(self, x):
        self.a.append(x) # 맨 끝에 추가
        i = len(self.a) -1 # 추가한 인덱스 (맨 끝 인덱스)
        # 부모 노드와의 비교(과정반복)
        while i > 0:
            p = (i-1)//2 # 부모노드 인덱스
            if self.a[p] > self.a[i]:
                self.a[p], self.a[i] = self.a[i], self.a[p]
                i = p
            else:
                break

    # 가장 첫 요소(최소값 추출 -> 삭제연산)
    def pop(self):
        if not self.a:  raise IndexError("pop from empty heap") # 배열이 비었으면 예외처리
        # 가장 첫 요소를 뽑는건 어렵지 않음. 그 다음 재배열하는게 중요
        first = self.a[0]
        last = self.a.pop()
        # 재배열

        if self.a: self.a[0] = last # 마지막 요소를 처음에 넣음(빈배열일경우 예외처리)
        # 왼쪽자식, 오른쪽 자식을 돌면서 더 작으면 교환
        i = 0 # 비교주체
        n = len(self.a)
        while True:
            l = (i*2)+1     # 왼쪽 자식
            r = (i*2)+2     # 오른쪽 자식

            if n <= l : # 자식이 더 이상 없을 때 (왼쪽자식인덱스와 배열의 마지막 인덱스 비교)
                break

            c = l 
            if r < n and self.a[l] > self.a[r]:
                c = r
    
            if self.a[i] > self.a[c] : # 왼쪽 자식과 비교
                self.a[i],self.a[c] =  self.a[c],self.a[i] # 자리바꾸기
                i = c
            else:
                break
        return first
        

            
            



h = MinHeap()
for x in [1,4,10,16,4,22,66,81,5,6,7,9,3,28]:
    h.push(x)

print(h.a)
while len(h):
    print(h.pop(), end =' ') 

