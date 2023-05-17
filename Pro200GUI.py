from tkinter import *
import sys

responseString = "ChatGPT Answer"

root = Tk()
root.geometry('400x400') #Size of form
root.configure(background= 'white')
root.title('ChatGPT Response')

lblTitle3 = Label(root, text="Chat's response: ")
lblTitle3.place(anchor=CENTER, relx=.5, rely=.5)

lblresponse = Label(root, text= responseString )
lblresponse.place(anchor=CENTER, relx=.5, rely=.6)

def close_window(event):
    sys.exit() 

root.bind("<Escape>", close_window)
root.mainloop()