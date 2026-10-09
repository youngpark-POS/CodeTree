from bisect import bisect_left # lower bound
from collections import deque

perfumes = []
next_idx = 0

def main():
    q = int(input())

    for _ in range(q):
        cmds = list(map(int, input().split()))
        cmd, args = cmds[0], cmds[1:]
        # print(cmd, args)

        if cmd == 1:
            n, s_list = args[0], args[1:]
            for idx, s in enumerate(s_list, start=1):
                perfumes.append((idx, s))
            next_idx = n+1

        elif cmd == 2:
            v = args[0]
            perfumes.append((next_idx, v))
            next_idx += 1

        elif cmd == 3:
            target = args[0]
            for i, (idx, s) in enumerate(perfumes):
                if idx == target:
                    del perfumes[i]
                    print(s)
                    break
            else:
                print(-1)
        
        elif cmd == 4:
            # scent-based BFS(0~K), O(K)
            k = args[0]
            visited = [1e9] * (k+1)
            q = deque()
            set_scents = set([p[1] for p in perfumes])
            # print(set_scents)
            for s in set_scents:
                if s > k:
                    continue
                q.append(s)
                visited[s] = 1
            
            while q:
                s = q.popleft()
                if s == k:
                    print(visited[s])
                    break
                for s2 in set_scents:
                    if s+s2 <= k and visited[s+s2] > visited[s]+1:
                        visited[s+s2] = visited[s]+1
                        q.append(s+s2)
            else:
                print(-1)

        elif cmd == 5:
            k = args[0]
            top = sorted([p[1] for p in perfumes])
            midbase = []
            for i in range(len(perfumes)):
                for j in range(len(perfumes)):
                    midbase.append(perfumes[i][1] + perfumes[j][1])
            midbase.sort()
            # print(top)
            # print(midbase)
            len_midbase = len(perfumes) ** 2
            cnt = 0
            for t in top:
                cnt += len_midbase - bisect_left(midbase, k-t)
            print(cnt)




if __name__ == "__main__":
    main()