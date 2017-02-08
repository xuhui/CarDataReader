import time
import json

#-------------------------------------------------------
#
# Gets values from OBD II connector
#
#
#---------------------------------------------------------

    filepath = "/home/pi/jasper-client/client/car_log/log_rpm.txt"
    file = open(filepath, "r")

    rpmLogs = json.loads(file.decode())


    if lastLog['timestamp'] > lastReadTime:
    return None