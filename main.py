# -*- coding: utf-8 -*-
# اختبار تشغيل Kivy – الخطوة الأولى

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class GeneralVIP(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.08, 1)  # خلفية داكنة
        return Label(
            text="🔥 General VIP شغال بنجاح 🔥",
            font_size="22sp",
            halign="center",
            valign="middle"
        )

if __name__ == "__main__":
    GeneralVIP().run()
