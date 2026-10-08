
def main():
    gems = []
    next_idx = 0
    n_cmds = int(input())

    for _ in range(n_cmds):
        cmds = list(map(int, input().split()))
        cmd, args = cmds[0], cmds[1:]

        if cmd == 1:
            n, g = args[0], zip(args[1::2], args[2::2])
            for idx, (w, v) in enumerate(g):
                gems.append((idx, w, v))
            next_idx = n
            gems.sort(key=lambda x: (-x[1], x[2]))

        elif cmd == 2:
            w, v = args
            for i in range(len(gems)):
                if gems[i][1] < w or gems[i][1] == w and gems[i][2] < v:
                    gems.insert(i, (idx, w, v))
                    break
            else:
                gems.append((idx, w, v))
        
        elif cmd == 3:
            target = args[0] - 1
            for idx, (i, w, v) in enumerate(gems):
                if idx == target:
                    print(v)
                    del gems[idx]
                    break
            else:
                print(-1)
        
        elif cmd == 4:
            #  0-1 knapsack
            pass

        elif cmd == 5:
            #  2-pointer
            d = args[0]
            if len(gems) == 0:
                print(0)
                continue
            front, back = 0, 1
            cnt = 0
            while front < back < len(gems):
                if gems[front][1] - gems[back][1] <= d:
                    cnt += 1
                    back += 1
                else:
                    front += 1
            cnt += (back-front-1)
            print(cnt)


if __name__ == "__main__":
    main()