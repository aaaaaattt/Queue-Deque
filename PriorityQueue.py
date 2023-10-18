class PriorityQueue :
    def __init__(self,capacity = 10) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0 #요소의 수

        def isEmpty(self) : return self.size == 0 #공백상태 = 요소의 수가 0

        def isFull(self) : return self.size == capacity #포화상태 = 요소의 수가 capacity랑 같다

        def enqueue(self, e) :
            if not self.isFull():
                self.array[self.size] = e #포화상태가 아니면 배열의 제일 뒤에 삽입
                self.size += 1

        def findMaxIndex(self) :        #우선순위 구하는 메소드
            if self.isEmpty(): return -1 #공백이면 -1 반환
            highest = 0
            for i in range(1, self.size) :
                if self.array[i] > self.array[highest] : #공백이 아니면 우선순위가 가장 높은 요소의 인덱스 highest를 구해반환
                    highest = i
            return highest
        
        def dequeue(self):                                                                              #우선순위가 가장 높은 요소 삭제
            highest = self.findMaxIndex()                                                                   #1. highest 요소를 찾고
            if highest != -1 :                                      
                self.size -= 1                                                                            #( 배열은 끝은 size - 1이므로 )
                self.array[highest], self.array[self.size]=self.array[self.size], self.array[highest]       #2. 이것을 마지막 요소와 교환(튜플 사용)
            return self.array[self.size]                                                                    #3. 마지막 요소를 반환
        
        def peek(self):
            highest = self.findMaxIndex()
            if highest != -1:
                return self.array[highest]
            
        def __str__(self):
            return str(self.array[0:self.size])