
# this script will run until closed and send notifications to the user to complete tasks
# this library is used to access the time() function
import time 

# import win10toast
from win10toast import ToastNotifier

# create an object called 'task' to the ToastNotifier class
task = ToastNotifier()

print("This program will send reminders during your shift once an hour", '\n')
print("*******Complete these tasks at the beginning of your shift*******", '\n')
print("Test Back-up Laptop")
print("X")
print("Inspect Server")
print("Check X")
print("Login Gmail & Customer Email")
print("Login X")
print("Login Splunk")
print("Check Splunk Email Alerts")
print("Login X")
print("Login X")
print("Login Solarwinds")
print("Review Solarwinds For Error Messages")
print("Open X Dashboards:")
print("Update X On Both Towers")
print("Review Work Orders")
print("Review Knowledgebase", '\n')

# loop will run as long as 12 hours have not passed
while True: 
    # if an hour has passed update all variables and instruct to check Work orders and SIEMs by sending a desktop notification
    task.show_toast("TASK", "Check X and Splunk & Follow-up on New Work Orders & Pending Work Orders", duration = 10)
    print("Check X and Splunk")
    print("Follow-up on New Work Orders & Pending Work Orders", '\n')
    time.sleep(3600)
      


