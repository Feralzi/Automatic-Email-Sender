import smtplib, ssl
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.base import runTouchApp
from time import time, sleep
from threading import Timer
import time
import datetime
from datetime import datetime, date
from datetime import timedelta
from datetime import date
from kivy.uix.checkbox import CheckBox 
from kivy.core.window import Window


#Follow the CAN-SPAM Act in the United States and other laws and regulations related to email marketing in your country.
#MADE BY Feralzi


class EmailSend(App):
    def build(self):
        Window.size = (600, 550)
        self.window = GridLayout()
        self.window.cols = 2
        self.window.size_hint = (0.7, 0.5)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.65}
        
        #add widgets to window-----------------------------------------------------

        #Layout Fix
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)

        #Icon
        self.window.add_widget(Image(source="email1.png",
                      size_hint=(None,None),
                      height = 60,
                      width= 200))



        #Layout Fix-------------------------
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------



        #Enter gmail
        self.creds = Label(text= "Gmail address:",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.gmail = TextInput(multiline=False,
                               size_hint=(None,None),
                               height = 30,
                               width= 200)
        self.window.add_widget(self.gmail)



        #Layout Fix-------------------------
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------


        
        #Enter password
        self.creds = Label(text="Password:",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)

        self.passw = TextInput(multiline=False,
                               password=True,
                               size_hint=(None,None),
                               height = 30,
                               width= 200)
        self.window.add_widget(self.passw)



        #Layout Fix-------------------------
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        
    
        #Enter message
        self.creds = Label(text="Message:",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)
                               
        self.msg = TextInput(multiline=False,
                             size_hint=(None,None),
                             height = 30,
                             width= 200)
        self.window.add_widget(self.msg)



        #Layout Fix-------------------------
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        

        #Enter reciever
        self.creds = Label(text="Reciever's mail:",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)
                               
        self.rvr = TextInput(multiline=False,
                             size_hint=(None,None),
                             height = 30,
                             width= 200)
        self.window.add_widget(self.rvr)



        #Layout Fix-------------------------
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        

        #Enter the amount of times to send
        self.creds = Label(text="Amount sending:",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)
                               
        self.amt = TextInput(multiline=False,
                              hint_text="X>1 is considered SPAM",
                              input_type= 'number',
                              input_filter= 'int',
                              size_hint=(None,None),
                              height = 30,
                              width= 200)
        self.window.add_widget(self.amt)



        #Layout Fix-------------------------
        self.creds = Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        

        #Sleep timer
        self.creds = Label(text="Sleep timer:",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)

        self.trueSec = bool(False)
        def on_checkbox_active_inactive(checkBoxSec, value):
            if value == True:
                print("Checkbox for 'seconds' is active")
                self.trueSec = value

                self.sec.disabled = False
                

            else:
                    self.sec.disabled = True
                    self.trueSec = False

            return self.trueSec
            return self.sec
        


        #Layout Fix-------------------------
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        

        self.creds = Label(text="Seconds",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        self.creds=Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        self.checkBoxSec = CheckBox(size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.checkBoxSec)
        self.checkBoxSec.bind(active = on_checkbox_active_inactive)

        #Layout Fix-------------------------
        self.sec = TextInput(multiline=False,
                                     input_type='number',
                                     input_filter='int',
                                     size_hint=(None,1.3),
                                     width = 100,
                                     hint_text="5 sec...",
                                     disabled= True)
        self.window.add_widget(self.sec)
        #Layout Fix-------------------------



        self.trueMin = bool(False)
        def on_checkbox_active_inactive1(checkBoxMin, value):
            if value == True:
                print("Checkbox for 'minutes' is active")
                self.trueMin = value
                self.min.disabled = False
                

            else:
                    self.min.disabled = True
                    self.trueMin = False

            return self.trueMin
            return self.min

            
        
        
        
        self.creds = Label(text="Minutes",
                           size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        self.creds =Label(text="",
                           size_hint=(None,None),
                           height = 10,
                           width= 200)
        self.window.add_widget(self.creds)
        #Layout Fix-------------------------
        self.checkBoxMin = CheckBox(size_hint=(None,None),
                           height = 30,
                           width= 200)
        self.window.add_widget(self.checkBoxMin)
        self.checkBoxMin.bind(active = on_checkbox_active_inactive1)
        #Layout Fix-------------------------
        self.min = TextInput(multiline=False,
                                     input_type='number',
                                     input_filter='int',
                                     size_hint=(None,1.3),
                                     width = 100,
                                     hint_text="2 min...",
                                     disabled= True)
        self.window.add_widget(self.min)
        
        
        
        #Enter button
        self.button = Button(text="Send!",
                             size_hint=(None,None),
                             height = 30,
                             width= 200)
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        


        return self.window
        return self.checkBoxSec
        
        

    def callback(self, instance):

        email = self.gmail.text
        passwords = self.passw.text

        mail = self.msg.text

        reciever = self.rvr.text

        port=465

        sslcontext=ssl.create_default_context()

        val = self.amt.text
        self.intAmt = int(val)

        for i in range(0,self.intAmt):

            connection = smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)

            connection.login(email,passwords)

            connection.sendmail(email,reciever,mail)

            print(str(i + 1) + str("/")+ str(self.intAmt))

            if (self.trueSec == True):
                valSec = self.sec.text
                self.intSec = int(valSec)
                time.sleep(self.intSec)

            if (self.trueMin == True):
                valMin = self.min.text
                self.intMin = int(valMin)
                time.sleep(self.intMin * 60)


        
        
if __name__ == "__main__":
    EmailSend().run()



