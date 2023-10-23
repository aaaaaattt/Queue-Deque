from CircularQueue import CircularQueue

def isValidPos(x,y) :
    if 0 <= x < MAZE_SIZE and 0<= y < MAZE_SIZE :   #(x,y)가 미로 내부이고
        if map[y][x] == '0' or map[y][x] =='x':     #갈 수 있는 칸(0)이거나 출구(x)이면 True
            return True
        return False                                #갈 수 없는 길은 False
    

def BFS() : #너비우선탐색 함수
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS:')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if(map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y-1) : que.enqueue((x, y-1)) #상
            if isValidPos(x, y+1) : que.enqueue((x, y+1)) #하
            if isValidPos(x-1, y) : que.enqueue((x-1, y)) #좌
            if isValidPos(x+1, y) : que.enqueue((x+1, y)) #우
    return False

map = [['1','1','1','1','1','1'],   #0 = 갈 수 있는 칸
       ['e','0','0','0','0','1'],   #1 = 벽. 막힌 칸
       ['1','0','1','0','1','1'],   #x = 출구
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]

MAZE_SIZE = 6

result = BFS()
if result : print('성공')
else : print('실패')