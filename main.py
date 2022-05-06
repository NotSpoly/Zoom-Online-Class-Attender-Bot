meeting_url = "Put In your Meeting URL here"

url = "Put in Your discord webhook here"


from datetime import datetime
import webbrowser
import requests
import time

def sendMessage(message):
    my_data = {"content": message}
    requests.post(url, data = my_data)

classJoined = "0"
remindedAlready = "False"

schedule ={
"09 00 00" : "Join your class",
"02 00 00" : "Break",
"03 00 00" : "Study now",
"05 00 00" : "Now you can play Valorant",
"06 00 00" : "End",
}
while True:
    hour = datetime.now().strftime('%H')
    timenow = datetime.now().strftime('%H %M %S')
    if  hour == "08" and classJoined=="0":
        webbrowser.open(meeting_url)
        sendMessage("Joined your online class")
        classJoined = "1"
    else:
        pass

    if hour == "15" and remindedAlready == "False":
        sendMessage("Reminder! Do you have an extra class today?")
        remindedAlready = "True"
    try:
        sendMessage(schedule[timenow])
        time.sleep(2)
    except:
        pass
