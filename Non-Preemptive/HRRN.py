import matplotlib.pyplot as plt

# [PID, Arrival Time, Burst Time]
procs = [[1, 0, 4], [2, 1, 3], [3, 2, 7], [4, 3, 2]]
n = len(procs)
completed = [False]*n
time, completed_count = 0, 0
wt, tat = [0]*n, [0]*n
gantt = []

while completed_count < n:
    idx = -1
    highest_rr = -1
    for i in range(n):
        at, bt = procs[i][1], procs[i][2]
        if not completed[i] and at <= time:
            rr = (time - at + bt) / bt
            if rr > highest_rr:
                highest_rr = rr
                idx = i
    if idx == -1:
        time += 1
        continue
    pid, at, bt = procs[idx]
    start = time
    wt[idx] = start - at
    tat[idx] = wt[idx] + bt
    time += bt
    gantt.append((start, pid, time))
    completed[idx] = True
    completed_count += 1

for i in range(n):
    print(f"P{procs[i][0]}: WT={wt[i]}, TAT={tat[i]}")
print("Avg WT:", sum(wt)/n)
print("Avg TAT:", sum(tat)/n)

# Gantt Chart
plt.figure()
for start, pid, end in gantt:
    plt.barh(0, end-start, left=start)
    plt.text(start + (end-start)/2, 0, f"P{pid}", ha='center')
plt.yticks([]); plt.xlabel("Time"); plt.title("Gantt Chart - HRRN"); plt.show()
