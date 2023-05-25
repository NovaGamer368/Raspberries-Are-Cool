from tkinter import *
import sys

responseString = "The Fitnessgram case is a legal dispute between the American College of Sports Medicine (ACSM) and the Cooper Institute over the use of the Fitnessgram physical fitness assessment. The ACSM sued the Cooper Institute for copyright infringement, claiming that the Cooper Institute had copied the Fitnessgram assessment without permission. The case was eventually settled out of court, with d the Cooper Institute over the use of the Fitnessgram physical fitness assess the Cooper Institute agreeing to pay a licensing fee to the ACSM for the use of the Fitnessgram atitute had copied the Fitnessgram assessment without permission. The case was ssessment.  "
def gui(response):
    root = Tk()
    root.geometry('800x500') #Size of form
    root.configure(background= "#302f2f")
    root.title('ChatGPT Response')

    frame_counter = Frame(root,background="#302f2f")
    frame_counter.grid(column=1, row=1)

    lblTitle3 = Label(frame_counter, text="Chat's response: ", justify=CENTER, font= "Arial 20", background="#302f2f", fg="#d03382")
    lblTitle3.pack(side=TOP)
    response = insert_newline(response)

    lblresponse = Label(frame_counter, text=response, justify=CENTER, background="#302f2f", fg="white", anchor=CENTER, padx= 1, pady=3, font="Arial 12")
    lblresponse.pack(side=BOTTOM)

    def close_window(event):
        sys.exit() 

    root.bind("<Escape>", close_window)
    root.mainloop()

def insert_newline(string):
    result = ""
    counter = 0

    for char in string:
        print (result)
        if counter >= 100 and char == " ":
            result += "\n"
            counter = 0
        else:
            result += char
            counter += 1

    return result

#gui(responseString)
