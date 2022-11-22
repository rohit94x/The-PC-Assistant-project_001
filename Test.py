from SpeechRecognitionCode import cl_SpeechRecognize
from pywinauto.application import Application

import time



class cl_AutomateApp:


    def fn_AutomateExe(OrderText,driver):


           print(OrderText)
           Otext=[]
           Otext=OrderText.split()
           if  Otext[1].lower() not in  'url':
                   if OrderText.lower() ==  "open notepad":
                    app = Application(backend='uia').start('notepad.exe')
                   elif OrderText.lower() == "open excel":
                    app = Application(backend='uia').start(r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe")
                   else :
                       print('Sorry  Not Recognized  Command, Can u repeat ')
           elif Otext[1].lower()  ==  'url':
                   if Otext[0].lower() == "youtube":
                       driver.get("https://www.youtube.com/")
                   elif Otext[0].lower() == "orange" :
                       driver.get("https://opensource-demo.orangehrmlive.com/")


