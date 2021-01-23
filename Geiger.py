import tkinter as tk
from tkinter import ttk
import random
from time import sleep
import pyaudio
import wave
import multiprocessing as mp

# Deal with the wave file importing etc and pyaudio setup.
CHUNK = 1024
audiopath = r"C:\Users\Dom\Desktop\Ringtonesalarms\124.wav"
wf = wave.open(audiopath, 'rb')
p = pyaudio.PyAudio()

def playgeiger():

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()
    stream.stop_stream()
    stream.close()


# Create Quit Button Callback
def quitbuttoncallback():
    root.destroy()

# Configure main window

root = tk.Tk()
root['padx'] = 100
root['pady'] = 50

# Box Text
textlabel = ttk.Label(text="Geiger Counter Frequency")
textlabel.pack()

# Set up scale bar
scalevar = tk.IntVar()
scalebar = ttk.Scale(variable=scalevar)
scalebar.pack()

# Create Quit Button
quitbutton = ttk.Button(text = "Quit",command=quitbuttoncallback)
quitbutton.pack()


while(True):
    # Program main logic on loop here...
    root.update()
    root.title(round(scalebar.get()*1000,0))
    randomnumber = random.random()
    # print(randomnumber)
    # print(f"{round(randomnumber,3)} and {round(scalebar.get(),3)}" )
    if randomnumber > scalebar.get():
        # print(randomnumber)
        # Do sound...
        mp.Process(target=playgeiger())
        print("geiger")
    # sleep(0.1)