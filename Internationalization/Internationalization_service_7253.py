import gettext
import locale
import os

class I18nService:
 def __init__(self, locale_path, default_locale):
 self.locale_path = locale_path
 self.default_locale = default_locale
 self.translation = gettext.translation('messages', localedir=self.locale_path, languages=[self.default_locale])
 self.translation.install()

 def set_locale(self, locale):
 self.translation = gettext.translation('messages', localedir=self.locale_path, languages=[locale])
 self.translation.install()

 def gettext(self, text):
 return self.translation.gettext(text)

 def ngettext(self, singular, plural, n):
 return self.translation.ngettext(singular, plural, n)

# Example usage:
locale_path = '/path/to/locale'
default_locale = 'en_US.UTF-8'
i18n = I18nService(locale_path, default_locale)

print(i18n.gettext('Hello, world!')) # Translated text based on default locale

i18n.set_locale('fr_FR.UTF-8') # Switch to French locale
print(i18n.gettext('Hello, world!')) # Translated text based on French locale
