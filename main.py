from pytube import *
from Tkinter import Tk, BOTH, END, Listbox, StringVar
from ttk import Frame, Button, Entry, Label

class Downloader(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		
		self.doGUI()
		
	
	def downloadvid(self):
		try:
			#Get video link from textbox
			self.yt = YouTube(self.yt_linkbox.get())
			print self.yt.videos
			#Download video at specified location in specified resolution and format
			self.ST_text.set("Downloading...")
			self.vid = self.yt.get(self.formatselect, self.resolutionselect)
			self.vid.download("/home")
			self.ST_text.set("Done.")
		except:
			self.ST_text.set("Error!")
		
		
	def option(self, val):
		#Get the selected option from listbox
		self.idx = self.resolutionlistbox.curselection()
		self.resolutionselect = self.resolutionlistbox.get(self.idx)
		
		#Set the format for the resolutions
		if self.resolutionselect == "144p":
			self.formatselect = "3gp"
		
		if self.resolutionselect == "240p":
			self.formatselect = "3gp"
			
		if self.resolutionselect == "360p":
			self.formatselect = "mp4"
			
		if self.resolutionselect == "480p":
			self.formatselect = "mp4"
			
		if self.resolutionselect == "720p":
			self.formatselect = "mp4"
		
		
	def doGUI(self):
		#Setup some stuff
		self.pack(fill=BOTH, expand=1)
		self.parent.title("Snail YouTube")
		
		#Textbox for entering YouTube link
		self.yt_linkbox = Entry(self, width = 30)
		self.yt_linkbox.place(x=100, y=10)
		
		#Button for downloading video
		self.downloadbutton = Button(self, text="Download!", command=self.downloadvid)
		self.downloadbutton.place(x=262, y=60)
		
		#List of resolutions
		self.resolutionlist = ["144p", "240p", "360p", "480p", "720p"]
		
		#Resolution listbox
		self.resolutionlistbox = Listbox(self)
		
		for i in self.resolutionlist:
			self.resolutionlistbox.insert(END, i)
		
		self.resolutionlistbox.bind("<<ListboxSelect>>", self.option)
		self.resolutionlistbox.pack(pady=35)
		
		#Adress text
		self.AT = Label(self, text="YouTube link:")
		self.AT.place(x=10, y=10)
		
		#Resolution text
		self.RT = Label(self, text="""Choose video
resolution:""")
		self.RT.place(x=10, y=50)
		
		#Status text
		self.ST_text = StringVar()
		self.ST_text.set("")
		self.ST = Label(self, textvariable=self.ST_text)
		self.ST.place(x=125, y=120)
		
		
def main():
	#Setup some more stuff
	root = Tk()
	root.geometry("350x150+300+300")
	app = Downloader(root)
	root.mainloop()
	
if __name__ == '__main__':
	main()
