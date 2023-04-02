import android
import pyttsx3
import threading
import time

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

droid = android.Android()

def speak(text):
    droid.ttsSpeak(text)

class MyBoxLayout(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.spacing = '10dp'
        self.padding = '10dp'
        
        self.btn = Button(text="Press and speak...")
        self.btn.bind(on_press=self.start_recognition)
        self.add_widget(self.btn)
    
    def start_recognition(self, instance):
        self.btn.text = "Listening..."
        t = threading.Thread(target=self.recognize)
        t.start()
    
    def recognize(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            self.btn.text = text
            speak(text)
        except:
            self.btn.text = "Could not recognize your voice."
    
class MyApp(App):
    
    def build(self):
        return MyBoxLayout()
