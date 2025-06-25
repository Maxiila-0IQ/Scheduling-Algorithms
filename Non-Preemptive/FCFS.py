import matplotlib.pyplot as plt

# [PID, Arrival Time, Burst Time]
procs = [[1, 0, 5], [2, 2, 3], [3, 4, 1], [4, 6, 2]]
n = len(procs)
procs.sort(key=lambda x: x[1])  # Sort by Arrival Time

time = 0
wt, tat = [0]*n, [0]*n
gantt = []

for i in range(n):
    pid, at, bt = procs[i]
    start = max(time, at)
    wt[i] = start - at
    tat[i] = wt[i] + bt
    time = start + bt
    gantt.append((start, pid, time))

for i in range(n):
    print(f"P{procs[i][0]}: WT={wt[i]}, TAT={tat[i]}")
print("Avg WT:", sum(wt)/n)
print("Avg TAT:", sum(tat)/n)

# Gantt Chart
plt.figure()
for start, pid, end in gantt:
    plt.barh(0, end-start, left=start)
    plt.text(start + (end-start)/2, 0, f"P{pid}", ha='center')
plt.yticks([]); plt.xlabel("Time"); plt.title("Gantt Chart - FCFS"); plt.show()
