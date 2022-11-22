import speech_recognition as sr


class cl_SpeechRecognize:


   def fn_RecognizeWord(self):
      r= sr.Recognizer()
      with sr.Microphone() as source:
        print('Speak Anything')
        audio= r.listen(source)
      try:
       text= r.recognize_google(audio)
       print('You said:{}'.format(text))
       return text
      except:
       print("sorry couldnt Recognize your Voice")


