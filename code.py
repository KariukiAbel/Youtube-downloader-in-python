from tkinter import *
from pytube import YouTube

root = Tk()
# setting the geometry of the GUI
root.geometry("400x350")
root.title("Youtube video downloader")


# defining download function
def download():
# using try and except to execute program without errors
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).stream.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")
        
        
Label(root, text="Welcome to abel's youtube downloader application", font="Consolas 15 bold").pack()
myVar = StringVar()
myVar.set("Enter the link below")


#create the Entry widget to ask the user to enter url
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()

#created the entry widget to get the link
Entry(root, textvariable=link, width=40).pack(pady=10)

Button(root, text="Download video", command=download).pack()

#running the mainloop
root.mainloop()
