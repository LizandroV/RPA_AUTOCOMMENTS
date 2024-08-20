import os
from datetime import datetime

link = "https://us02web.zoom.us/j/82652378554?pwd=VFp3ekxXck9rRTNqMnQ2bUZkU0NhUT09"

print("CERRAR PROCESOS")
os.system('taskkill /f /im firefox.exe')
os.system('taskkill /f /im zoom.exe')
sleep(2)

try:
    print("Abrir Firefox")
    App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    sleep(5)
    type("l",KEY_CTRL)
    sleep(2)
    paste(link)
    sleep(2)
    type(Key.ENTER)
    sleep(20)
    wait("1690238757424.png",10)
    click(Pattern("1690238312947.png").targetOffset(102,4))
    sleep(2)
    click("1690238358418.png")
    sleep(2)
    type("v",KEY_ALT)
    sleep(2)
    os.system('taskkill /f /im firefox.exe')
    print("FIN")
except:
    exc_type, exc_val, exc_tb = sys.exc_info()
    ErrorText = "***** ERROR IN SCRIPTNAME = " + sys.argv[0] + " *****\n"
    ErrorText += "Date/Time : " + str(datetime.now()) + "\n"
    ErrorText += "Line Number: " + str(exc_tb.tb_lineno) + "\n"
    ErrorText += "Error Type : " + exc_type.__name__ + "\n"
    ErrorText += "Error Value: " + exc_val.message + "\n"
    ErrorText += "***************************************************************\n\r"
    print ErrorText