#Python 2
try:
    import Tkinter as tk
#Python 3
except ImportError:
    import tkinter as tk

class NotificationWindow(tk.Frame):
    """ Notifcations window"""

    def __init__(self, _anime, master = None):
        super().__init__(master)
        
        self.grid(row=0,column=0)

        # Set the notifications window on lower right
        """
        w  = 200  
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width/2) - (w/2)
        y = (screen_height/2) - (w/2)
        self.master.geometry(("%dx%d+%d+%d"% (w, w, x, y)))
        """
        self.master.resizable(False,False)

        anime = _anime

        self.create_window(anime)

    def create_window(self, _anime):
        
        window = tk.Toplevel(self.master)
        window.title("Notification %s"%(_anime))

        notification = tk.Label(window, text="%s"%(_anime), padx = 20, pady= 20)
        notification.grid(row=0,column=0)