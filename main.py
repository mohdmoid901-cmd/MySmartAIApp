import time
import threading
import urllib.parse
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class SmartAIApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.ai_running = True
        
        self.output_screen = TextInput(readonly=True, text="[AI System Initialized] Waiting for notifications...\n")
        self.add_widget(self.output_screen)
        
        threading.Thread(target=self.background_ai_loop, daemon=True).start()

    def mock_notification_listener(self):
        return [
            {"package": "com.whatsapp", "sender": "Rahul", "text": "Are we meeting tonight for dinner?"},
            {"package": "com.instagram", "sender": "Pooja", "text": "Send me the photos of yesterday's party!"}
        ]

    def background_ai_loop(self):
        while self.ai_running:
            notifications = self.mock_notification_listener()
            for notif in notifications:
                app_pkg = notif["package"]
                sender = notif["sender"]
                msg_text = notif["text"]
                
                reply = self.process_ai_reply(sender, msg_text)
                if reply:
                    log_msg = f"[Notification Match] App: {app_pkg.split('.')[-1].upper()} | From: {sender} | Msg: {msg_text}\n🤖 [AI Automated Auto-Reply Sent]: {reply}\n"
                    Clock.schedule_once(lambda dt, m=log_msg: self.update_log(m))
            time.sleep(10)

    def process_ai_reply(self, sender, text):
        try:
            prompt = f"Act as a smartphone auto-reply assistant. The user is busy. Reply to {sender} who said '{text}' in just 1 short, casual, and friendly sentence."
            encoded_prompt = urllib.parse.quote(prompt)
            url = f"https://pollinations.ai{encoded_prompt}"
            
            response = requests.get(url, timeout=8)
            if response.status_code == 200:
                return response.text.strip()
        except Exception:
            pass
        
        text_lower = text.lower()
        if "hello" in text_lower or "hi" in text_lower:
            return f"Hi {sender}, I am away from my phone right now."
        return f"Hi {sender}, I am busy right now. Will text you back soon!"

    def update_log(self, message):
        self.output_screen.text += f"\n{message}"

class MyApp(App):
    def build(self):
        self.ui = SmartAIApp()
        return self.ui
    def on_stop(self):
        self.ui.ai_running = False

if __name__ == '__main__':
    MyApp().run()
  
