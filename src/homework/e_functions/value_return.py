from datetime import datetime

#get current day
dt = datetime.today()
epoch_seconds = dt.timestamp()
#print(seconds)

def get_hour(epoch_seconds):
    hours = epoch_seconds // 3600
    remHours = hours % 3600
    #print("Remainder hr: ", remHours)
    return remHours

def get_minutes(epoch_seconds):
    minutes = epoch_seconds // 60
    remMinutes = minutes % 60
    #print("Remainder min: ", remMinutes)
    return remMinutes

def get_seconds(epoch_seconds):
    seconds = epoch_seconds % 3600
    remSeconds = seconds % 60
    #print("Remainder sec: ", remSeconds)
    return remSeconds