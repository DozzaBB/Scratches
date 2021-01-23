from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:\\Users\\Dom\\Desktop\\HLD",title = "Select file")
file = open(root.filename,"rb")
text = file.read()
filesfound = 0
i=0
while i<len(text):
    i+=1
    if (text[i:i+4].decode("utf-8",errors='ignore')=="RIFF"):
        percent = "{:.1f}".format(i / len(text) * 100)
        print(f"Parsed {percent} percent")
        filesize = int.from_bytes(text[i+4:i+7],byteorder='little')
        endpos = i+filesize
        output = open(f"{filesfound}.wav","w+b")
        contents = text[i:endpos]
        output.write(contents)
        print(f"Saved file as {filesfound}.wav")
        filesfound+=1
        i = endpos-10 #for good measure
        output.close
print("..Done!")
