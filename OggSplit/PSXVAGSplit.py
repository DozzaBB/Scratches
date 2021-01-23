from tkinter import filedialog
from tkinter import *
import time

root = Tk()
root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Dom\Desktop", title="Select file")
file = open(root.filename, "rb")
root.destroy()  # kill it
print("Processing file...")
text = file.read()
totalsize = len(text)
filesfound = 0
starttime = time.time()
print(f"Started at timecode = {starttime}")
i = 0 #counter to parse through file.
while i < totalsize:
    i += 1
    if text[i:i + 4] == b'VAGp':  # found VAGp likely.
        print(f"VAG header found at {hex(i)}")
        #i is the start of the VAG file.
        waveformsize = text[i+8:i+8+4]
        print(f"waveform is of size {waveformsize}")
        waveform = text[i+]
                    endpos = y + 4
                    contents = text[i-1:endpos + offset]
                    output = open(f"{filesfound}.png", "w+b")
                    output.write(contents)
                    filesfound += 1
                    output.close
                    i = endpos  # speed up processing significantly.
                    percent = i / len(text) * 100
                    stoptime = time.time()
                    predtime = "{:.1f}".format((stoptime - starttime) / (percent / 100) - (
                                stoptime - starttime))  # linear forecast of the length of the program, then subtract the runtime so far
                    # spit out some probably useful info for ya butt
                    print("------------------------------------------")
                    print(f"Parsed {percent}% of file so far")
                    print(f"Remaining time: {predtime} sec")
                    print(f"Saved file as {filesfound}.png")
                    print(f"filesize is {len(contents)} bytes")
                    print("------------------------------------------")
print("..Done!")
