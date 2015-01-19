#coding=utf-8
import Tkinter as tk
import ttk
from normalConfig import NormalConfig
import subprocess

def tail(f , n) :
    """
     tail the n lines of f
     not process exception
    """
    blockSize = 256
    blockLineNum = 0 
    block = ""
    blockstart = 0
    startPos = f.tell()
    f.seek(0 , 2) # jump to end
    curPos = f.tell()

    while curPos > startPos : 
        curPos -= blockSize 
        if curPos < startPos :
            curPos = startPos
        f.seek(curPos)
        block = f.read()
        blockLineNum = block.count("\n")
        if blockLineNum > n :
            break
    for i in range(blockLineNum - n + 1) :
        blockstart = block.find('\n' , blockstart) + 1
    return block[blockstart:]
def createTextWithScroll(master , row=0 , col=0 , rowspan=1 , colspan=30) :
    scroll = ttk.Scrollbar(master)
    scroll.grid(row=row , column=colspan-1 , sticky=tk.N+tk.S)
    logText = tk.Text(master , state=tk.DISABLED)
    logText.grid(row=row , column=col , columnspan=colspan - 1 , sticky=tk.N+tk.S+tk.E+tk.W)
    scroll.config(command=logText.yview)
    logText.config(yscrollcommand=scroll.set)
    NormalConfig.setTextTag(logText)
    logText.config(cursor="arrow")
    return logText 
def openFileFolder(path , system) :
    print path
    print system
    if system == "Windows" :
        try :
            subprocess.Popen("explorer /select," + path , shell=True)
        except :
            pass
    elif system == "Linux" :
        try :
            subprocess.Popen("nautilus "+ path , shell=True)
        except Exception , e:
            print e
            pass
    elif system == "OSX" :
        try :
            subprocess.Popen("open " + os.path.dirname(path) , shell=True)
        except :
            pass
    
    
if __name__ == "__main__" :
    f = open(__file__)
    print tail(f,10) 
