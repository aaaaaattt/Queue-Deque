map = [['1','1','1','1','1','1'],   #0 = 갈 수 있는 칸
       ['e','0','0','0','0','1'],   #1 = 벽. 막힌 칸
       ['1','0','1','0','1','1'],   #x = 출구
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]

MAZE_SIZE = 6

def isValidPos(x,y) :
    if 0 <= x < MAZE_SIZE and 0<= y < MAZE_SIZE :   #(x,y)가 미로 내부이고
        if map[y][x] == '0' or map[y][x] =='x':     #갈 수 있는 칸(0)이거나 출구(x)이면 True
            return True
        return False                                #갈 수 없는 길은 False