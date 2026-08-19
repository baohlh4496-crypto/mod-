import tkinter as tk
from tkinter import ttk


def calculate_and_display_metrics(processes, completion_times, start_times):
    n = len(processes)

   
    tat_list = []  
    wt_list = [] 
    rt_list = []  

    for i in range(n):
        arrival = processes[i]["arrival"]
        burst = processes[i]["burst"]
        ct = completion_times[i]
        st = start_times[i]

        tat = ct - arrival
        wt = tat - burst
        rt = st - arrival

        tat_list.append(tat)
        wt_list.append(wt)
        rt_list.append(rt)

   
    avg_tat = sum(tat_list) / n
    avg_wt = sum(wt_list) / n
    avg_rt = sum(rt_list) / n

    root = tk.Tk()
    root.title("Bảng Kết Quả Lập Lịch CPU (Metrics & Results Table)")
    root.geometry("780x380")

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill="both", expand=True)

    columns = (
        "pid",
        "arrival",
        "burst",
        "completion",
        "tat",
        "wt",
        "rt",
    )
    tree = ttk.Treeview(
        frame, columns=columns, show="headings", height=n + 2
    )

    
    headers = {
        "pid": "PID",
        "arrival": "Arrival Time (AT)",
        "burst": "Burst Time (BT)",
        "completion": "Completion Time (CT)",
        "tat": "Turnaround Time (TAT)",
        "wt": "Waiting Time (WT)",
        "rt": "Response Time (RT)",
    }

    for col, text in headers.items():
        tree.heading(col, text=text)
        tree.column(col, width=110, anchor="center")

    
    for i in range(n):
        tree.insert(
            "",
            "end",
            values=(
                processes[i]["pid"],
                processes[i]["arrival"],
                processes[i]["burst"],
                completion_times[i],
                tat_list[i],
                wt_list[i],
                rt_list[i],
            ),
        )

   
    tree.insert(
        "",
        "end",
        values=("---", "---", "---", "---", "---", "---", "---"),
    )

   
    tree.insert(
        "",
        "end",
        values=(
            "Trung bình",
            "-",
            "-",
            "-",
            f"{avg_tat:.2f}",
            f"{avg_wt:.2f}",
            f"{avg_rt:.2f}",
        ),
    )

    
    scrollbar = ttk.Scrollbar(
        frame, orient=tk.VERTICAL, command=tree.yview
    )
    tree.configure(yscroll=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


if __name__ == "__main__":
    sample_processes = [
        {"pid": "P1", "arrival": 0, "burst": 10},
        {"pid": "P2", "arrival": 1, "burst": 1},
        {"pid": "P3", "arrival": 2, "burst": 2},
        {"pid": "P4", "arrival": 3, "burst": 1},
        {"pid": "P5", "arrival": 4, "burst": 5},
    ]

    
    sample_completion_times = [19, 2, 7, 4, 14]
    sample_start_times = [0, 1, 5, 3, 9]

    
    calculate_and_display_metrics(
        sample_processes, sample_completion_times, sample_start_times
    )
