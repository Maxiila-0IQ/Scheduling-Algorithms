import matplotlib.pyplot as plt
from collections import deque

procs = [[1, 0, 5], [2, 1, 3], [3, 2, 1], [4, 3, 2]]  # [PID, AT, BT]
quantum = 2
n = len(procs)
bt = [bt for _, _, bt in procs]
rt = bt[:]
wt, tat = [0]*n, [0]*n
time, complete, gantt = 0, 0, []
q = deque()
in_q = [False]*n

while complete < n:
    for i in range(n):
        if procs[i][1] <= time and not in_q[i] and rt[i] > 0:
            q.append(i)
            in_q[i] = True
    if not q:
        time += 1
        continue
    idx = q.popleft()
    in_q[idx] = False
    start = time
    run = min(quantum, rt[idx])
    rt[idx] -= run
    time += run
    gantt.append((start, procs[idx][0], time))
    for i in range(n):
        if procs[i][1] <= time and not in_q[i] and rt[i] > 0:
            q.append(i)
            in_q[i] = True
    if rt[idx] > 0:
        q.append(idx)
        in_q[idx] = True
    else:
        complete += 1
        tat[idx] = time - procs[idx][1]
        wt[idx] = tat[idx] - bt[idx]

for i in range(n):
    print(f"P{procs[i][0]}: WT={wt[i]}, TAT={tat[i]}")
print("Avg WT:", sum(wt)/n)
print("Avg TAT:", sum(tat)/n)

# Gantt Chart
plt.figure()
for start, pid, end in gantt:
    plt.barh(0, end-start, left=start)
    plt.text(start+(end-start)/2, 0, f"P{pid}", ha='center')
plt.yticks([]); plt.xlabel("Time"); plt.title("Gantt Chart - Round Robin"); plt.show()
