import time
import json

#-------------------------------------------------------
#
# Gets values from OBD II connector
#
#
#---------------------------------------------------------

def rpmFetchUnreadOverloads(lastReadTime):
    filepath = "/home/pi/jasper-client/client/car_log/log_rpm.txt"
    file = open(filepath, "r")

    rpmLogs = json.loads(file.decode())

    lastLog = rpmLogs[rpmLogs.length - 1]

    if lastLog['timestamp'] > lastReadTime:
        return lastLog
    return None