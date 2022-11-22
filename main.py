from selenium import webdriver
import sys
sys.path.append(r'C:\Users\hp\PycharmProjects\PythonAssistant\chromedriver_win32\chromedriver.exe')

from SpeechRecognitionCode import cl_SpeechRecognize
from AutomateWindowCode import cl_AutomateApp

class  cl_main():

   def __init__(self):
         self.OrderText = cl_SpeechRecognize.fn_RecognizeWord(self)
         self.driver = webdriver.Chrome(r"C:\Users\hp\PycharmProjects\PythonAssistant\chromedriver_win32\chromedriver.exe")

   def main(self):

         cl_AutomateApp.fn_AutomateExe(self.OrderText)
         cl_AutomateApp.fn_AutomateURL(self.OrderText,self.driver)



if __name__ == '__main__':
    o_m=cl_main()
    o_m.main()
