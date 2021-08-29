from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog,Text
root=tk.Tk()


apps=[]
def addapp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename=filedialog.askopenfilename(initialdir='/',title="Select File",filetypes=(("text","*.txt"),("all files","*.*")))
    apps.append(filename)
    for app in apps:
        label=tk.Label(frame,text="HIT RUN NOW \n ",font=50,fg="black",bg="lightgreen",height=30)
        label.pack()


def run():
    for app in apps:
        fh=open(app,'r')
        mytext=fh.read()
        output=gTTS(text=mytext,tld='us',lang='en')
        output.save("text_to_speech.wav")
        #print(output.text)
        os.system("start text_to_speech.wav")
        question()

def question():
    for widget in frame.winfo_children():
        widget.destroy()
    label=tk.Label(frame,text="wanna try again? \n ",fg="Blue",bg="lightgreen",font=70,height=10)
    label.pack()
    yesagain=tk.Button(frame,text="YES",fg="black",bg="yellow",command=Yes,activebackground='blue',width=20)
    yesagain.pack()
    noagain=tk.Button(frame,text="NO",fg="black",bg="pink",command=No,activebackground='gray',width=20)
    noagain.pack()
    

def Yes():
    addapp()
def No():
    root.destroy()
#canvas
canvas=tk.Canvas(root,height=500,width=800,bg="#263D42",confine=False)
canvas.pack()
frame=tk.Frame(canvas,height=500,width=800,bg="lightgreen")
label=tk.Label(frame,font=50,text="TEXT TO SPEECH",fg="red",bg="lightgreen",height=10)
label.pack()


frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
#adding button
openfile=tk.Button(frame,text="Open File",fg="white",bg="#263D42",command=addapp,activebackground='pink',pady=18,width=10)
openfile.pack()
#running button
runtest=tk.Button(root,text="Run",fg="white",bg="black",command=run,width=110,activebackground='yellow')
runtest.pack()



root.mainloop()

#######

    
