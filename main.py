# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.08, 0.1, 1)

KV = '''
ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        padding: 40
        spacing: 20

        Label:
            text: "General VIP"
            font_size: "30sp"
            size_hint_y: None
            height: 80

        TextInput:
            hint_text: "البريد الإلكتروني"
            multiline: False

        TextInput:
            hint_text: "كلمة المرور"
            password: True
            multiline: False

        TextInput:
            hint_text: "رقم الهاتف"
            multiline: False
            input_filter: "int"

        Button:
            text: "تسجيل الدخول"
            size_hint_y: None
            height: 55
            background_color: (0.2, 0.5, 0.9, 1)
            on_press: app.root.current = "home"

<HomeScreen>:
    name: "home"
    BoxLayout:
        Label:
            text: "🎉 تم الدخول بنجاح"
            font_size: "24sp"
'''

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class GeneralVIPApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    GeneralVIPApp().run()
