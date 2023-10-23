import math
from PriorityQueue import PriorityQueue
from isValidPos import isValidPos

(ax,ay) = (5,4)
def dist(x,y):
    (dx, dy) = (ax-x,ay-y)
    return math.sqrt(dx*dx + dy*dy)

def MySmartSearch() :
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here
        if(map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y-1) : q.enqueue((x, y-1)) #상
            if isValidPos(x, y+1) : q.enqueue((x, y+1)) #하
            if isValidPos(x-1, y) : q.enqueue((x-1, y)) #좌
            if isValidPos(x+1, y) : q.enqueue((x+1, y)) #우
        print('우선순위큐 :',q)
    return False

map = [['1','1','1','1','1','1'],   #0 = 갈 수 있는 칸
       ['e','0','0','0','0','1'],   #1 = 벽. 막힌 칸
       ['1','0','1','0','1','1'],   #x = 출구
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]

MAZE_SIZE = 6

a = MySmartSearch()
print(a)