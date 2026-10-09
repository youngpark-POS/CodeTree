from copy import deepcopy
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  #  up, right, down, left

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def get_adjacent_sea(board, px, py, d):
    d_list = (d, (d+3)%4, (d+1)%4, (d+2)%4)
    for new_d in d_list:
        nx, ny = px+dx[new_d], py+dy[new_d]
        if is_valid(nx, ny, len(board)) and board[nx][ny] == 0:
            return (nx, ny, new_d)
    return (-1, -1, -1)


def find_nearest_sea(board, px, py):
    newboard = deepcopy(board)
    q = deque()
    q.append((px, py, 0))
    newboard[px][py] = 3
    candidates = []
    min_dist = 1e9
    while q:
        x, y, dist = q.popleft()
        for d in (3, 2, 1, 0):
            nx, ny = x+dx[d], y+dy[d]
            if not is_valid(nx, ny, len(newboard)) or newboard[nx][ny] in (1, 3):
                continue
            elif newboard[nx][ny] == 0:
                if dist+1 > min_dist:
                    continue
                elif dist+1 < min_dist:
                    min_dist = dist+1
                    candidates = []
                candidates.append((nx, ny))
                newboard[nx][ny] = 3
            else:
                q.append((nx, ny, dist+1))
                newboard[nx][ny] = 3

    return (-1, -1) if not candidates else min(candidates, key=lambda x: (x[0], x[1]))


def get_nearest_sea(board, px, py, tx, ty):
    # search order dir 3-2-1-0
    newboard = deepcopy(board)
    q = deque()
    q.append((px, py, 0))
    newboard[px][py] = 3
    while q:
        x, y, d = q.popleft()
        if (x, y) == (tx, ty):
            return (x, y, d)
        for d in (3, 2, 1, 0):
            nx, ny = x+dx[d], y+dy[d]
            if not is_valid(nx, ny, len(newboard)) or newboard[nx][ny] in (1, 3):
                continue
            q.append((nx, ny, d))
            newboard[nx][ny] = 3
    return (-1, -1, -1)


def main():
    n, r, c, d = list(map(int, input().split()))
    #  d (1상, 2하, 3좌, 4우) -> (0상, 2하, 3좌, 1우)
    d_map = (-1, 0, 2, 3, 1)
    d = d_map[d]
    x, y = r-1, c-1

    # 0 for not visited sea, 1 for obstacles, 2 for visited sea
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    board[x][y] = 2
    print(x+1, y+1)
    
    while True:
        nx, ny, nd = get_adjacent_sea(board, x, y, d)
        if (nx, ny, nd) != (-1, -1, -1):
            x, y, d = nx, ny, nd
            print(x+1, y+1)
            board[x][y] = 2
            continue
        nx, ny = find_nearest_sea(board, x, y)
        if (nx, ny) == (-1, -1):
            break
        _, _, nd = get_nearest_sea(board, x, y, nx, ny)
        x, y, d = nx, ny, nd
        print(x+1, y+1)
        board[x][y] = 2
        

if __name__ == "__main__":
    main()