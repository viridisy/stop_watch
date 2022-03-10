from enum import Flag
import tkinter as tk
import time

def buttonClick():
    global stop_watch
    if not stop_watch["start"]:
        stop_watch["start"]=True
        stop_watch["startTime"]=time.time()- stop_watch["elapsed"]
        button1.config(text="stop")
        button1.pack()
    else:
        stop_watch["start"]=False
        button1.config(text="start")
        button1.pack()
        


def resetClick():
    global stop_watch
    stop_watch["start"]=False
    stop_watch["elapsed"]=0
    stop_watch["startTime"]=0
    button1.config(text="start")

def topClick():
    global flag
    if not flag:
        flag=True
        root.attributes("-topmost", True)
        button3.config(text="解除")
        button3.pack()
    else:
        flag=False
        root.attributes("-topmost", False)
        button3.config(text="最前面")
        button3.pack()

def update():
    global stop_watch
    if stop_watch["start"]:
        n = time.time() 
        stop_watch["elapsed"]=n-stop_watch["startTime"]
        
    min=stop_watch["elapsed"]//60
    sec=stop_watch["elapsed"]%60
    label1.config(text="{:.0f}:".format(min)+"{:02.0f}".format(sec))
    label1.pack()
    root.after(100, update)  

def upload():
    f=open("log.txt", "a")
    now=time.ctime()
    cnvtime=time.strptime(now)
    f.writelines(time.strftime("%Y/%m/%d %H:%M, ", cnvtime)+label1["text"]+"\n")
    f.close()
    resetClick()

stop_watch = {
    "start":False,
    "startTime":0.0,
    "elapsed":0.0
}

flag=False
root = tk.Tk()
root.geometry("150x210")

button2 = tk.Button(
    root, text="reset",
    command = resetClick,
    width=15, height=2,
    anchor="center"
)
button2.pack()

button1 = tk.Button(
    root, text="start",
    command=buttonClick,
    width=15, height=2,
    anchor="center"
)
button1.pack()

label1=tk.Label(
    root,text="",
    font=("MSゴシック","30", "bold"),
    anchor="center"
)

label1.pack()

button4=tk.Button(
    root, text="upload",
    command=upload,
    width=15, height=2
)

button3=tk.Button(
    root, text="最前面",
    command=topClick,
    width=7, height=1
)
button3.pack()
button4.pack()
root.after(100, update)
root.mainloop()