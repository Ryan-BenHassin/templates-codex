#TODO
import locale
import gettext
import os
import tkinter as tk
from tkinter import ttk

class InternationalizationService:
 def __init__(self, locale_path, locale_name):
 self.locale_path = locale_path
 self.locale_name = locale_name
 self.locale.setlocale(locale.LC_ALL, self.locale_name)
 self.translation = gettext.translation('base', localedir=self.locale_path, languages=[self.locale_name])

 def translate(self, text):
 return self.translation.gettext(text)

def main():
 locale_path = '../locales'
 locale_name = 'en_US'
 service = InternationalizationService(locale_path, locale_name)

 root = tk.Tk()
 root.title("Internationalization Service")

 ttk.Label(root, text=service.translate("Hello")).pack()
 ttk.Label(root, text=service.translate("World!")).pack()

 root.mainloop()

if __name__ == "__main__":
 main()
