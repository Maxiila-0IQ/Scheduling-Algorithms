import matplotlib.pyplot as plt

# [PID, Arrival Time, Burst Time]
procs = [[1, 0, 6], [2, 1, 8], [3, 2, 7], [4, 3, 3]]
n = len(procs)
procs.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival, then burst
completed = [False]*n
time, completed_count = 0, 0
wt, tat = [0]*n, [0]*n
gantt = []

while completed_count < n:
    idx = -1
    min_bt = float('inf')
    for i in range(n):
        if not completed[i] and procs[i][1] <= time and procs[i][2] < min_bt:
            idx = i
            min_bt = procs[i][2]
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
plt.yticks([]); plt.xlabel("Time"); plt.title("Gantt Chart - SJF (Non-Preemptive)"); plt.show()
