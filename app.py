import tkinter as tk 
from tkinter import font
from topoSort import topoSort
from time import sleep

numberOfTasks = 0 
tasks = []
ar = {}
nodeTaskMap = {}
TaskDurationMap = {} 
TaskNodeMap = {}
curr_i = 0
curr_j = 0
curr_selected_option = 0 

def displayTopoOrdering(topo):
    infoLabel = tk.Label(window, text="Tasks presented horizontally can be executed in parallel", bg="white", relief="solid", borderwidth=1, highlightbackground="black", highlightthickness=1,  font=font.Font(size=12), padx=20, pady=20)
    infoLabel.pack(pady=40)

    frame = tk.Frame(window, width=200, height=500, bg="white", highlightbackground="black", highlightthickness=1, )
    frame.pack(pady=40, padx=40)

    label = tk.Label(frame, text="A VALID ORDERING OF TASKS")
    label.pack(padx=4, pady=4)
    totalTimeTaken = 0 
    if len(topo) == 0: 
        print("Here ")
        label.config(text="CYCLE EXISTS, TASKS CANNOT BE ORDERED")
    for i in range(len(topo)): 
        levelFrame = tk.Label(frame,width=200, height=40, bg="white")
        levelFrame.pack(pady=4, padx=2)
        maxi = 0 
        for j in topo[i]:
            taskLabel = tk.Label(levelFrame, text=nodeTaskMap[j], bg="white",  relief="solid", borderwidth=1, highlightthickness=1, highlightbackground="black", padx=4, pady=4)
            taskLabel.pack(side="left", padx=4, pady=2)
            maxi = max(maxi, TaskDurationMap[nodeTaskMap[j]])
        totalTimeTaken += maxi 
        durationLabel = tk.Label(levelFrame, text=f"Duration : {maxi}")
        durationLabel.pack(side="left", padx=4, pady=2)
        if i != len(topo)-1:
            arrowLabel = tk.Label(frame, text="↓", bg="white")
            arrowLabel.pack()
    totalTimeTakenLabel = tk.Label(window, bg="white", relief="solid", borderwidth=1, highlightbackground="black", highlightthickness=1,  font=font.Font(size=12), width=20, height=2, text=f"Total Time: {totalTimeTaken}")
    totalTimeTakenLabel.pack(padx=5, pady=10) 
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def on_radio_button_click(var):
    global curr_selected_option
    selected_option = var.get()
    if selected_option == 1:
        print("Option 1 selected")
    elif selected_option == 2:
        print("Option 2 selected")
    elif selected_option == 3:
        print("Option 3 selected")
    curr_selected_option = var.get()

def waitForButtonClick(button_clicked):
    global ar, curr_i, curr_j 
    print(curr_i, curr_j)
    if curr_selected_option == 1: 
        ar[curr_i].append(curr_j)
    
    elif curr_selected_option == 2: 
        ar[curr_j].append(curr_i) 
    
    print(ar)
    button_clicked.set(True)

def inputGraph():
    global ar, curr_i, curr_j 
    for i in range(numberOfTasks+1):
        ar[i] = []
    print(ar)

    frame = tk.Frame(window, width=500,height=500 ,  highlightbackground="black",)
    frame.pack(padx=40, pady=40)

    labels_frame = tk.Frame(frame)
    labels_frame.pack()

    task1Label = tk.Label(labels_frame, text="", bg="white",  relief="solid", borderwidth=1, highlightthickness=1, highlightbackground="black", padx=10, pady=10)
    task1Label.pack(side="left", padx=10, pady=10)
    andLable = tk.Label(labels_frame, text="and")
    andLable.pack(side="left")
    task2Label = tk.Label(labels_frame, text="", bg="white",  relief="solid", borderwidth=1, highlightthickness=1, highlightbackground="black", padx=10, pady=10)
    task2Label.pack(side="left", padx=10, pady=10)

    var = tk.IntVar()

    radios_frame = tk.Frame(frame)
    radios_frame.pack(padx=20, pady=20)

    radio_button1 = tk.Radiobutton(radios_frame, text="Before", variable=var, value=1, command=lambda : on_radio_button_click(var))
    radio_button1.pack(side="left", padx=10, pady=10)

    radio_button2 = tk.Radiobutton(radios_frame, text="After", variable=var, value=2, command=lambda : on_radio_button_click(var))
    radio_button2.pack(side="left", padx=10, pady=10)

    radio_button3 = tk.Radiobutton(radios_frame, text="Unrelated", variable=var, value=3, command=lambda : on_radio_button_click(var))
    radio_button3.pack(side="left", padx=10, pady=10)

    button_clicked = tk.BooleanVar()

    nextTaskButton = tk.Button(frame, text="Next", command=lambda : waitForButtonClick(button_clicked), borderwidth=2, width = 8, bg = "#d9d5d4")
    nextTaskButton.pack(padx=20, pady=20)
    


    for i in range(numberOfTasks):
        for j in range(i+1, numberOfTasks):
            curr_i = i+1
            curr_j = j+1
            button_clicked.set(False)
            task1Label.config(text=tasks[i])
            task2Label.config(text=tasks[j])
            window.wait_variable(button_clicked)

    frame.destroy()

    print(ar)
    topoTasks = topoSort(numberOfTasks, ar)
    print("topoTasks -> ", topoTasks)
    displayTopoOrdering(topoTasks)

def assignMap():
    global nodeTaskMap, TaskNodeMap
    for i in range(numberOfTasks):
        nodeTaskMap[i+1] = tasks[i]
        TaskNodeMap[tasks[i]] = i+1
    print(nodeTaskMap)

def storeTasks(tasksEntries, tasksFrame, durationEntries): 
    for i in range(numberOfTasks):
        tasks.append(tasksEntries[i].get())
        TaskDurationMap[tasksEntries[i].get()] = int(durationEntries[i].get())
    print(tasks)
    print("TaskDuration map ", TaskDurationMap)
    tasksFrame.destroy()
    assignMap()
    inputGraph()
    

def inputTasks():
    global tasks 
    tasksFrame = tk.Frame(window, height=500, width=200)
    tasksFrame.pack(padx=40, pady=40)
    enterTasksLabel = tk.Label(tasksFrame, text="Enter the tasks") 
    enterTasksLabel.pack()
    tasksEntries = []
    durationEntries = []
    print("No. of tasks ", numberOfTasks)
    for i in range(numberOfTasks):
        taskFrame = tk.Frame(tasksFrame, width=100, height=20, padx=4,pady=4)
        taskFrame.pack(padx=5, pady=5)
        taskLabel = tk.Label(taskFrame, text=f"Task {i+1} : ",)
        taskLabel.pack(side="left", padx=5, pady=5)
        taskEntry = tk.Entry(taskFrame, width=80, font=font.Font(size=12))
        taskEntry.pack(side="left", padx=5, pady=5)
        tasksEntries.append(taskEntry)
        durationLabel = tk.Label(taskFrame, text=f"Duration : ",)
        durationLabel.pack(side="left", padx=5, pady=5)
        durationEntry = tk.Entry(taskFrame, width=10, font=font.Font(size=12))
        durationEntry.pack(side="left", padx=5, pady=5)
        durationEntries.append(durationEntry)
    
    
    enterTasksButton = tk.Button(tasksFrame, text="Next", command = lambda : storeTasks(tasksEntries, tasksFrame, durationEntries), borderwidth=2, width = 8, bg = "#d9d5d4")
    enterTasksButton.pack(padx=5, pady=5)

    

def setNumberOfTasks(numberOfTasksFrame):
    global numberOfTasks 
    numberOfTasks = int(numberOfTasksEntry.get())
    print(numberOfTasks)
    numberOfTasksFrame.destroy()
    inputTasks()

if __name__ == '__main__':

    window = tk.Tk()
    window.state('zoomed')

    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=12)

    window.title("Project Planner")

    window.geometry("1500x700")

    titleLabel = tk.Label(window, text="PROJECT PLANNER", font=font.Font(size=16), bg="#ebeced", relief="solid", borderwidth=1, highlightbackground="black", highlightthickness=1, padx=20, pady=20)
    titleLabel.pack(fill=tk.X)

    numberOfTasksFrame = tk.Frame(window, height=200, width=200)
    numberOfTasksFrame.pack(padx=20, pady=20)
    
    introLabel = tk.Label(numberOfTasksFrame, text="Resolves task dependencies and provides an efficent ordering of tasks considering parallel processing", bg="white", relief="solid", borderwidth=1, highlightbackground="black", highlightthickness=1,  font=font.Font(size=12), padx=20, pady=20)
    introLabel.pack(pady=40,)

    numberOfTasksLabel = tk.Label(numberOfTasksFrame, text="Enter the number of tasks")
    numberOfTasksLabel.pack(pady=10)

    numberOfTasksEntry = tk.Entry(numberOfTasksFrame, font=font.Font(size=12))
    numberOfTasksEntry.pack()

    numberOfTasksButton = tk.Button(numberOfTasksFrame, text="Next", command=lambda:setNumberOfTasks(numberOfTasksFrame), borderwidth=2, width = 8, bg = "#d9d5d4")
    numberOfTasksButton.pack(pady=10)

    window.mainloop()
