# Task Remeinder with Notifications

import time

tasks = {"Submit project": 1, "Meeting with team": 10}
print("Task Reminder System Started!")

for task, delay in tasks.items():
    time.sleep(delay) #Simulates waiting until the task is due
    print(f"Reminder: {task} is due now!")
