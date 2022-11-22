from SpeechRecognitionCode import cl_SpeechRecognize
from pywinauto.application import Application

import time



class cl_AutomateApp:


    def fn_AutomateExe(OrderText):
           print(OrderText)
           if OrderText.lower() ==  "open notepad":
            app = Application(backend='uia').start('notepad.exe')
           elif OrderText.lower() == "open excel":
            app = Application(backend='uia').start(r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe")
           else :
               print('Sorry  Not Recognized  Command, Can u repeat ')




    def fn_AutomateURL(OrderText,driver):

            if OrderText.lower() == "open youtube":
                driver.get("https://www.youtube.com/")
            elif OrderText.lower() == "open orange":
                driver.get("https://opensource-demo.orangehrmlive.com/")


