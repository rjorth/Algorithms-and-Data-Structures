import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt


#pie chart for progress
remaining = 57.5
completed = 100-remaining

run_labels = "Completed", 'Distance Remaining'
run_sizes = [completed, remaining]
explode = (0,0)

fig1, ax1 = plt.subplots()
ax1.pie(run_sizes, explode=explode, labels=run_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()


progress = 26.25
weight_remaining = 100 - progress
weight_labels = "Progress", "Remaining"
weight_sizes = [progress, weight_remaining]

fig2, ax2 = plt.subplots()
ax2.pie(weight_sizes, labels=weight_labels, colors=['orange','grey'], autopct='%1.1f%%', shadow=True, startangle=90) 
ax2.axis('equal')
plt.show()