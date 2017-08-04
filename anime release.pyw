"""
Made by Tiago Tquelim 
sikozonbatata@gmail.com

Searches for animes in www.9anime.to and returns the newly updated ones with
the respectiev link to it. 
"""

from threading import Timer
import tkinter as tk
import urllib.parse
import urllib.request
import re
import time
import webbrowser


class Application(tk.Frame):
	
	def __init__(self, master = None):
		super().__init__(master)
		self.pack()
		self.master.title("Anime Updater")

		self._headers = {}
		self._headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		self.url = "https://9anime.to/updated"

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


	def getAnimes(self):
		request = urllib.request.Request(self.url, headers = self._headers)
		response = urllib.request.urlopen(request)
		responseData = response.read()

		self.search = re.findall(r'" class="name">(.*?)</a>', str(responseData))
		self.links = re.findall(r'</a> <a href="(.*?)" class="name">', str(responseData))

	def refresh(self):
		self.getAnimes()
		self.showAnimes()
		self.master.after(3000, self.refresh)


if __name__ == "__main__":
		
		app = Application() 

		

		
		
		
		
