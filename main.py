# -*- coding: utf-8 -*-
# General VIP - Version 1
# تطبيق تجريبي للتأكد أن Kivy شغال

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# ضبط حجم افتراضي (مفيد للاختبار)
Window.clearcolor = (0.08, 0.08, 0.1, 1)

class MainTabs(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_default_tab = False
        self.tab_pos =  top_mid 
        self.background_color = (0.1, 0.1, 0.12, 1)

        # التبويب 1
        self.add_widget(self.make_tab("الرئيسية", "🔥 General VIP شغال بنجاح 🔥"))

        # التبويب 2
        self.add_widget(self.make_tab("الشبكة", "📶 Network Monitor"))

        # التبويب 3
        self.add_widget(self.make_tab("الخدمات", "⚙️ USSD / SMS / Mode"))

        # التبويب 4
        self.add_widget(self.make_tab("الإعدادات", "🛠️ Settings"))

    def make_tab(self, title, text):
        from kivy.uix.tabbedpanel import TabbedPanelItem

        tab = TabbedPanelItem(text=title)
        box = BoxLayout(orientation= vertical , padding=20)

        label = Label(
            text=text,
            font_size=20,
            halign="center",
            valign="middle"
        )
        label.bind(size=label.setter( text_size ))

        box.add_widget(label)
        tab.add_widget(box)
        return tab


class GeneralVIPApp(App):
    def build(self):
        self.title = "General VIP"
        return MainTabs()


if __name__ == "__main__":
    GeneralVIPApp().run()
        
