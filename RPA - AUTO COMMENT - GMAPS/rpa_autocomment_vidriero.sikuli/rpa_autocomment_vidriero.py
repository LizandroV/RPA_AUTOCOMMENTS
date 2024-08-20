import os
from datetime import datetime

link = "https://g.page/r/CdgWWQDRA41SEBM/review"

print("CERRAR PROCESOS")
os.system('taskkill /f /im firefox.exe')
sleep(2)

try:
    print("ABRIR FIREFOX")
    App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    sleep(15)
    type("l",KEY_CTRL)
    sleep(2)
    paste(link)
    sleep(2)
    type(Key.ENTER)
    App.open("C:\\TSC\\Data\\rpa_autocomments\\Email.exe")
    sleep(30)
    click(Pattern("1691525937921.png").targetOffset(-162,80))
    type("v",KEY_CTRL)
    sleep(2)
    type(Key.ENTER)
    sleep(2)
    App.open("C:\\TSC\\Data\\rpa_autocomments\\Pass.exe")
    sleep(25)
    if exists("1689614451059.png",5):
        click(Pattern("1689614451059.png").targetOffset(-117,15))
        sleep(5)
        if exists("1689614599059.png",5):
            click("1689614609693.png")
        else:
            type("w",KEY_CTRL)
            sleep(2)
            type("w",KEY_CTRL)
    type("v",KEY_CTRL)
    sleep(2)
    type(Key.ENTER)
    sleep(2)
    print("INGRESAR COMENTARIO")
    App.open("C:\\TSC\\Data\\rpa_autocomments\\CommentVidriero.exe")
    sleep(25)
    if exists("1689627403396.png",5):
        type("w",KEY_CTRL)
        sleep(2)
        type("w",KEY_CTRL)

    elif exists("1689614705385.png",5):
        click("1689613800949.png")
        sleep(2)
    elif exists("1689615211435.png",5):
        type("w",KEY_CTRL)
        sleep(2)
        type("w",KEY_CTRL)
    if exists(Pattern("1689627598892.png").similar(0.90)):
        print("YA HAY COMENTARIO")
        type("w",KEY_CTRL)
        sleep(2)
        type("w",KEY_CTRL)
        print("FIN")
        
    elif exists(Pattern("1689702472275.png").similar(0.90),5):
        print("NO HAY COMENTARIO")
        click(Pattern("1689702472275.png").targetOffset(104,4))
        sleep(2)
        click(Pattern("1689613980876.png").targetOffset(-180,2))
        sleep(2)
        type("v",KEY_CTRL)
        sleep(2)
        click(Pattern("1689614187710.png").targetOffset(60,4))
        sleep(5)
        click(Pattern("1689626582142.png").targetOffset(-69,-2))
        sleep(2)
        type("w",KEY_CTRL)
        print("FIN")
        
    elif exists(Pattern("1689712696212.png").similar(0.90),5):
        print("NO HAY COMENTARIO 2")
        click(Pattern("1689712696212.png").targetOffset(97,-7))
        sleep(2)
        click(Pattern("1689613980876.png").targetOffset(-180,2))
        sleep(2)
        type("v",KEY_CTRL)
        sleep(2)
        click(Pattern("1689614187710.png").targetOffset(60,4))
        sleep(5)
        click(Pattern("1689626582142.png").targetOffset(-69,-2))
        sleep(2)
        type("w",KEY_CTRL)
        print("FIN")
        
except:
    App.open("C:\\TSC\\Data\\rpa_autocomments\\SSmail.exe")
    exc_type, exc_val, exc_tb = sys.exc_info()
    ErrorText = "***** ERROR IN SCRIPTNAME = " + sys.argv[0] + " *****\n"
    ErrorText += "Date/Time : " + str(datetime.now()) + "\n"
    ErrorText += "Line Number: " + str(exc_tb.tb_lineno) + "\n"
    ErrorText += "Error Type : " + exc_type.__name__ + "\n"
    ErrorText += "Error Value: " + exc_val.message + "\n"
    ErrorText += "***************************************************************\n\r"
    print ErrorText