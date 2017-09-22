#Python 2
try:
    import Tkinter as tk
    from plyer import notification as n
#Python 3
except ImportError:
    import tkinter as tk
    from plyer import notification as n

def notify(_anime):
    notification_logo = "notification.ico"
    n.notify(title= _anime,
             message= 'New episode out!',
             app_name = "Anime Scrapper",
             app_icon= notification_logo)
