from CircularQueue import *

class CircurlarDeque(CircularQueue): #자식클래스 ( 부모클래스 )
    def __init__(self,capacity = 10):
        super().__init__(capacity)  #super()를 이용해 부모의 생성자 호출.

        # isEmpty(),isFull(), size(), __str__() -> CircularQueue와 동일하므로 구현할 필요 X
        
        def addRear(self,item): #동작은 같지만 이름이 달라지므로 메소드를 다시 만들어야 함.
            self.enqueue(item)  #부모 클래스의 해당 연산 호출
        def deleteFront(self,item):
            return self.dequeue()
        def getFront(self):
            return self.peek()
        
        #새로 구현이 필요한 연산들
        def addFront(self,item) :
            if not self.isFull():
                self.array[self.front] = item                                   #전단 삽입은 덱이 포화상태가 아닌 경우 처리 가능
                self.front = (self.front -1 + self.capacity) % self.capacity    #현재의 front에 새로운 요소를 저장한 다음 front를 반시계 방향으로 한 칸 회전
                return item
            else:pass
        
        def deleteRear(self):                                                   #후단 삭제는 공백이 아닌 경우 처리가능.
            if not self.isEmpty():                                              #현재의 rear의 요소를 저장한 후, rear를 반식계 방향으로 한 칸 회전,
                item = self.array[self.rear]                                    #마지막으로 저장된 요소를 반환
                self.rear = (self.rear - 1 + self.capacity) % self.capacity
                return item
            else: pass

        def getRear(self ):
            if not self.isEmpty():
                return self.array[self.rear]    #후단 참조는 현재의 rear 요소 반환
            else:pass
