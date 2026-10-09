

def main():
    gems = []
    next_idx = 0
    n_cmds = int(input())

    for _ in range(n_cmds):
        cmds = list(map(int, input().split()))
        # print(cmds)
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
                if w > gems[i][1]:
                    gems.insert(i, (next_idx, w, v))
                    break
            else:
                gems.append((next_idx, w, v))
            next_idx += 1
        
        elif cmd == 3:
            target = args[0] - 1
            for idx, (i, w, v) in enumerate(gems):
                if i == target:
                    print(v)
                    del gems[idx]
                    break
            else:
                print(-1)
        
        elif cmd == 4:
            #  0-1 knapsack
            max_w = args[0]
            dp = [[0] * (max_w+1) for _ in range(len(gems)+1)]
            for i, (idx, w, v) in enumerate(gems, start=1):
                for new_w in range(max_w-w+1):
                    dp[i][new_w] = max(dp[i-1][new_w], dp[i-1][new_w+w] + v)
            print(max(dp[-1]))

        elif cmd == 5:
            #  2-pointer

            d = args[0]
            if len(gems) <= 1:
                print(0)
                continue
            front, back = 0, 1
            cnt = 0
            while back < len(gems):
                if gems[front][1] - gems[back][1] <= d:
                    back += 1
                else:
                    cnt += (back-front-1)
                    front += 1
            while front < back:
                cnt += (back-front-1)
                front += 1
            print(cnt)


if __name__ == "__main__":
    main()