import matplotlib.pyplot as plt

# [PID, Arrival Time, Burst Time, Priority (lower = higher priority)]
procs = [[1, 0, 8, 2], [2, 1, 4, 1], [3, 2, 9, 3], [4, 3, 5, 2]]
n = len(procs)
rt = [bt for _, _, bt, _ in procs]
wt, tat = [0]*n, [0]*n
time, complete, gantt, prev = 0, 0, [], -1

while complete < n:
    idx = -1
    for i in range(n):
        if procs[i][1] <= time and rt[i] > 0:
            if idx == -1 or procs[i][3] < procs[idx][3]:  # Lower number = higher priority
                idx = i
    if idx == -1:
        time += 1
        continue
    rt[idx] -= 1
    if prev != idx:
        gantt.append((time, procs[idx][0]))
        prev = idx
    if rt[idx] == 0:
        complete += 1
        finish = time + 1
        tat[idx] = finish - procs[idx][1]
        wt[idx] = tat[idx] - procs[idx][2]
    time += 1

for i in range(n):
    print(f"P{procs[i][0]}: WT={wt[i]}, TAT={tat[i]}")
print("Avg WT:", sum(wt)/n)
print("Avg TAT:", sum(tat)/n)

# Gantt Chart
plt.figure()
for i, (start, pid) in enumerate(gantt):
    end = gantt[i+1][0] if i+1 < len(gantt) else time
    plt.barh(0, end-start, left=start)
    plt.text(start+(end-start)/2, 0, f"P{pid}", ha='center')
plt.yticks([]); plt.xlabel("Time"); plt.title("Gantt Chart - Priority Scheduling"); plt.show()
