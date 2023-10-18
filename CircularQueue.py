class CircularQueue :
        def __init__(self, capacity = 8) :      #생성자
            self.capacity = capacity
            self.array = [None] * capacity
            self.front = 0
            self.rear = 0

        def isEmpty(self) :
            return self.front == self.rear  #front와 rear가 같으면 공백상태
        
        def isFull(self) :
            return self.front == (self.rear+1)%self.capacity #front가 self의 다음 위치이면 포화상태
        
        def enqueue(self, item):
            if not self.isFull():                           #포화상태가 아닌 경우 삽입 가능
                self.rear = (self.rear +1) % self.capacity  #rear를 시계방향으로 회전
                self.array[self.rear] = item                #그 자리에 새로운 요소를 저장!
            else: pass

        def dequeue(self) :
            if not self.isEmpty():                          #공백이 아닌 경우 삭제 가능
                self.front = (self.front+1)%self.capacity        #front를 시계방향으로 회전
                return self.array[self.front]               #삭제할 요소를 반환!
            
        def peek(self):
            if not self.isEmpty():                                  #공백이 아닌 경우
                return self.array[(self.front+1) % self.capacity]   #제일 앞에있는 요소 반환
            else: pass                                              #front는 변하지 않는다!

        def size(self) :                                                     #큐의 전체 요소의 수 계산
            return (self.rear - self.front + self.capacity) % self.capacity  #선형 큐와 달리 음수가 될 수 있으므로 추가로 용량을 더한 후에 계산
        
        def __str__(self) :
            if self.front < self.rear :
                return str(self.array[self.front+1:self.rear+1]) #slice기능 - self.front +1 : self.rear+1 의 범위는 self.front+1 ~ self.rear 범위!
            else :                                               #(마지막 요소 전까지)
                return str(self.array[self.front+1:self.capacity] + self.array[0:self.rear+1])
            
q = CircularQueue(8)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.enqueue('D')
q.enqueue('E')
q.enqueue('F')
print('A B C D E F 삽입 :', q)