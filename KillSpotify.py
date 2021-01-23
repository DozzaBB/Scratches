import os
import psutil

for process in psutil.process_iter():
    if "spotify" in process.name().lower():
        try:
            os.system(f"taskkill /F /PID {process.pid}")
        except:
            print(f"couldnt kill Process {process.name()} with PID {process.pid}")
os.system("start C:/Users/Dom/AppData/Roaming/Spotify/spotify.exe")
