from tkinter import filedialog
from tkinter import *
import time

root = Tk()
root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Dom\Desktop\HLD", title="Select file")
file = open(root.filename, "rb")
root.destroy()  # kill it
print("Processing file...")
text = file.read()
totalsize = len(text)
filesfound = 0
starttime = time.time()
print(f"Started at timecode = {starttime}")
i = 0
while i < totalsize:
    i += 1
    if text[i-1:i + 3] == b'\x89PNG':  # found png likely.
        if text[i + 11:i + 15]== b'IHDR':  # check for more header
            print(f"PNG header found at {hex(i)}")
            y = i
            filenotfound = 1
            while filenotfound:
                y += 1
                if text[y:y + 4] == b'IEND':  # look for the PNG end of file flag
                    offset = int.from_bytes(text[y - 5:y - 1],
                                            byteorder='little')  # account for the end of file chunk length.
                    filenotfound = 0
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
