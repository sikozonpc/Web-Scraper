"""
Made by Tiago Tquelim 
sikozonbatata@gmail.com

Searches for animes in www.9anime.to and returns the newly updated ones with
the respectiev link to it. 
"""

#Python 2
try:
    #import urllib2
    import Tkinter as tk
#Python 3
except ImportError:
    import tkinter as tk

from io import BytesIO
from PIL import Image, ImageTk, ImageOps
import base64
import urllib.parse
import urllib.request
import re
import time
import webbrowser


wishlist = ["Boruto"]



class NotificationWindow(tk.Frame):
    """ Notifcations window"""

    def __init__(self, _anime, master = None):
        super().__init__(master)
        self.pack()

        anime = _anime


        self.create_window(anime)


    def create_window(self, _anime):
        
        window = tk.Toplevel(self.master)
        window.title("Notification %s"%(_anime))

        notification = tk.Label(window, text="%s"%(_anime))
        notification.pack(side="top", fill="both", expand=True, padx=100, pady=100)



class Application(tk.Frame):
    """ Application main window"""
    
    
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.master.title("Anime Updater")
        
        self._headers = {}
        self._headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        self.url = "https://9anime.to/updated"


        self.current_anime = ""
        self.last_anime = "" 
        self.output = [""]
        
        self.refresh()
        self.master.mainloop()

    def showAnimes(self):

        print("check")

        for widget in self.winfo_children():
            widget.destroy()

        self.anime1 = tk.Button(self, text = self.search[0])
        self.anime1["command"] = lambda: webbrowser.open(self.links[0])
        self.anime1.pack(side="top")

        self.anime2 = tk.Button(self, text = self.search[1])
        self.anime2["command"] = lambda: webbrowser.open(self.links[1])
        self.anime2.pack(side="top")

        self.anime3 = tk.Button(self, text = self.search[2])
        self.anime3["command"] = lambda: webbrowser.open(self.links[2])
        self.anime3.pack(side="top")

        self.anime4 = tk.Button(self, text = self.search[3])
        self.anime4["command"] = lambda: webbrowser.open(self.links[3])
        self.anime4.pack(side="top")

        self.anime5 = tk.Button(self, text = self.search[4])
        self.anime5["command"] = lambda: webbrowser.open(self.links[4])
        self.anime5.pack(side="top")

        self.anime6 = tk.Button(self, text = self.search[5])
        self.anime6["command"] = lambda: webbrowser.open(self.links[5])
        self.anime6.pack(side="top")

        self.anime6 = tk.Button(self, text = self.search[6])
        self.anime6["command"] = lambda: webbrowser.open(self.links[6])
        self.anime6.pack(side="top")

        self.anime7 = tk.Button(self, text = self.search[7])
        self.anime7["command"] = lambda: webbrowser.open(self.links[7])
        self.anime7.pack(side="top")

        self.anime8 = tk.Button(self, text = self.search[8])
        self.anime8["command"] = lambda: webbrowser.open(self.links[8])
        self.anime8.pack(side="top")

        self.anime9 = tk.Button(self, text = self.search[9])
        self.anime9["command"] = lambda: webbrowser.open(self.links[9])
        self.anime9.pack(side="top")


    def getAnimes(self):
        request = urllib.request.Request(self.url, headers = self._headers)
        response = urllib.request.urlopen(request)
        responseData = response.read()

        # Fitler the anime names and links from the source code
        self.search = re.findall(r'" class="name">(.*?)</a>', str(responseData))
        self.links = re.findall(r'</a> <a href="(.*?)" class="name">', str(responseData))

        # List of animes got for manipulation
        self.output = self.search

    def refresh(self):

        self.last_anime = self.output[0]

        self.getAnimes()

        self.current_anime = self.output[0]

        print("Current anime: ",self.current_anime," last anime: ",self.last_anime)

        self.showAnimes()

        # Shows a notification if there is a new anime on the list
        if (self.current_anime != self.last_anime):
            self.notification(self.current_anime)

        # This is a timer to keep repeting
        self.master.after(5000, self.refresh)

    def getImage(self):
        url  = "https://d3ieicw58ybon5.cloudfront.net/full/u/d64566db23fc4454a80d1fd41606d2f1.jpg"

        # Get the URL based image from the Internet
        request = urllib.request.urlopen(url)
        img_byt = BytesIO(request.read())
        
        # Read into a memory stream
        image = Image.open(img_byt)
        image = ImageOps.fit(image, (200,250), method=0, bleed=0.0, centering=(0.5, 0.5)) 
       
        self.finalImg = ImageTk.PhotoImage(image)

        return self.finalImg
        
    def showImage(self, _image):
        """Displays a interface for the user to interact with the more recent animes"""

        # Displaying images
        self.label1 = tk.Label(image = _image )
        self.label1.pack(side = "right", anchor="w")

        self.label2 = tk.Label(image = _image )
        self.label2.pack(side = "right", anchor="w")

        self.label3 = tk.Label(image = _image )
        self.label3.pack(side = "right", anchor="w")

        self.label4 = tk.Label(image = _image )
        self.label4.pack(side = "right", anchor="w")

        self.label5 = tk.Label(image = _image )
        self.label5.pack(side = "right", anchor="w")

        # Second row

        self.label6 = tk.Label(image = _image )
        self.label6.pack(side = "left",anchor="s")

        self.label7 = tk.Label(image = _image )
        self.label7.pack(side = "left",anchor="s")

        self.label8 = tk.Label(image = _image )
        self.label8.pack(side ="left",anchor="s")

        self.label9 = tk.Label(image = _image)
        self.label9.pack(side = "left",anchor="s")

        self.label10 = tk.Label(image = _image )
        self.label10.pack(side = "left",anchor="s")

    def notification(self, _anime):
        """ Starts a new window to notify the user that a new episode is out """

        notify = NotificationWindow(_anime)




if __name__ == "__main__":
    
        app = Application() 


        

        
        
        
        
