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
import urllib.parse
import urllib.request
import re
import webbrowser


wishlist = ["Boruto"]


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
        self.master.resizable = False

        anime = _anime

        self.create_window(anime)

    def create_window(self, _anime):
        
        window = tk.Toplevel(self.master)
        window.title("Notification %s"%(_anime))

        notification = tk.Label(window, text="%s"%(_anime), padx = 20, pady= 20)
        notification.grid(row=0,column=0)



class Application(tk.Frame):
    """ Application main window"""
    
    
    def __init__(self, master = None):
        super().__init__(master)
        self.grid(row=0, column=0)
        self.master.title("Anime Updater")
        self.master.resizable = False
        #Status bar
        self.status = tk.Label(text = "",  bd = 1, relief = tk.SUNKEN)
        self.status.grid(row = 0,column=0)
        self.status.rowconfigure(0, weight=1)
        self.status.columnconfigure(0, weight=1)
        self.status.grid(sticky="news")
        
        self._headers = {}
        self._headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        self.url = "https://9anime.to/updated"


        self.current_anime = ""
        self.last_anime = "" 
        self.output = [""]
        

        self.refresh()
        self.master.mainloop()

    def showStatus(self, text, color="blue"):
        self.status["bg"]   = color
        self.status["text"] =  text

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

        self.showStatus(text= "REFRESHING... EXPECT LAG")
        print("a")
        
        self.last_anime = self.output[0]

        self.getAnimes()

        self.current_anime = self.output[0]

        print("Current anime: ",self.current_anime," last anime: ",self.last_anime)


        #Status the user that is refreshing and may the UI
        
        #Display thumbnails 
        imageUrl1 = self.getImagesUrl(0)
        self.image1 = self.getImage(imageUrl1)

        imageUrl2 = self.getImagesUrl(1)
        self.image2 = self.getImage(imageUrl2)

        imageUrl3 = self.getImagesUrl(2)
        self.image3 = self.getImage(imageUrl3)

        imageUrl4 = self.getImagesUrl(3)
        self.image4 = self.getImage(imageUrl4)

        imageUrl5 = self.getImagesUrl(4)
        self.image5 = self.getImage(imageUrl5)

        imageUrl6 = self.getImagesUrl(5)
        self.image6 = self.getImage(imageUrl6)

        imageUrl7 = self.getImagesUrl(6)
        self.image7 = self.getImage(imageUrl7)

        imageUrl8 = self.getImagesUrl(7)
        self.image8 = self.getImage(imageUrl8)

        imageUrl9 = self.getImagesUrl(8)
        self.image9 = self.getImage(imageUrl9)

        imageUrl10 = self.getImagesUrl(9)
        self.image10 = self.getImage(imageUrl10)

        self.showImage()

        # Shows a notification if there is a new anime on the list
        if (self.current_anime != self.last_anime):
            self.notification(self.current_anime)

        #Clear the status bar
        print("b")
        self.showStatus(text="...", color="grey")


        # This is a timer to keep repeting (time in miliseconds) 5mins for the release version
        self.master.after(10000, self.refresh)

    def getImagesUrl(self, _index):

        request = urllib.request.Request(self.url, headers = self._headers)
        response = urllib.request.urlopen(request)
        responseData = response.read()

        self.imagesURL = re.findall(r'&amp;url=(.*?)" alt="', str(responseData))

        return self.imagesURL[_index]

    def getImage(self, _url):
        #url  = "https://d3ieicw58ybon5.cloudfront.net/full/u/d64566db23fc4454a80d1fd41606d2f1.jpg"
        url = _url
        # Get the URL based image from the Internet
        request = urllib.request.urlopen(url)
        img_byt = BytesIO(request.read())
        
        # Read into a memory stream
        image = Image.open(img_byt)
        image = ImageOps.fit(image, (200,250), method=0, bleed=0.0, centering=(0.5, 0.5)) 
       
        self.finalImg = ImageTk.PhotoImage(image)

        return self.finalImg
        
    def showImage(self):
        """Displays a interface for the user to interact with the more recent animes"""

        for widget in self.winfo_children():
            widget.destroy()

        # Displaying images
        self.label1 = tk.Button(image = self.image1 ,command = lambda: webbrowser.open(self.links[0]))
        self.label1.grid(row=2, column=0, padx= 5, pady=5 )
        #Label with the name of the anime
        self.name1 = tk.Label(text = self.search[0]).grid(row=1, column=0)

        self.label2 = tk.Button(image = self.image2 ,command = lambda: webbrowser.open(self.links[1]))
        self.label2.grid(row=2, column=1, padx= 5, pady=5 )
        self.name2 = tk.Label(text = self.search[1]).grid(row=1, column=1)

        self.label3 = tk.Button(image = self.image3 ,command = lambda: webbrowser.open(self.links[2]))
        self.label3.grid(row=2, column=2, padx= 5, pady=5 )
        self.name3 = tk.Label(text = self.search[2]).grid(row=1, column=2)


        self.label4 = tk.Button(image = self.image4 ,command = lambda: webbrowser.open(self.links[3]))
        self.label4.grid(row=2, column=3, padx= 5, pady=5 )
        self.name4 = tk.Label(text = self.search[3]).grid(row=1, column=3)

        self.name3
        self.label5 = tk.Button(image = self.image5 ,command = lambda: webbrowser.open(self.links[4]))
        self.label5.grid(row=2, column=4, padx= 5, pady=5 )
        self.name5 = tk.Label(text = self.search[4]).grid(row=1, column=4)


    # Second row

        self.label6 = tk.Button(image = self.image6 ,command = lambda: webbrowser.open(self.links[5]) )
        self.label6.grid(row=4, column=0, padx= 5, pady=5 )
        self.name6 = tk.Label(text = self.search[5]).grid(row=3, column=0)

        self.label7 = tk.Button(image = self.image7 ,command = lambda: webbrowser.open(self.links[6]))
        self.label7.grid(row=4, column=1, padx= 5, pady=5 )
        self.name3 = tk.Label(text = self.search[6]).grid(row=3, column=1)

        self.label8 = tk.Button(image = self.image8 ,command = lambda: webbrowser.open(self.links[7]))
        self.label8.grid(row=4, column=2, padx= 5, pady=5 )
        self.name3 = tk.Label(text = self.search[7]).grid(row=3, column=2)

        self.label9 = tk.Button(image = self.image9,command = lambda: webbrowser.open(self.links[8]))
        self.label9.grid(row=4, column=3, padx= 5, pady=5 )
        self.name3 = tk.Label(text = self.search[8]).grid(row=3, column=3)

        self.label10 = tk.Button(image = self.image10 ,command = lambda: webbrowser.open(self.links[9]))
        self.label10.grid(row=4, column=4, padx= 5, pady=5 )
        self.name3 = tk.Label(text = self.search[9]).grid(row=3, column=4)


    def notification(self, _anime):
        """ Starts a new window to notify the user that a new episode is out """

        notify = NotificationWindow(_anime)




if __name__ == "__main__":
    
        app = Application() 


        

        
        
        
        
