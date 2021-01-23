import glob
import os
import eyed3




path = "E:/Dom/Music/Music/**"
for file in glob.glob(path, recursive=True):
    if file[len(file) - 4:] == ".mp3":
        file = file.replace("\\", "/")
        audio = eyed3.load(file)
        trackno = audio.tag.track_num[0]
        title = audio.tag.title
        if title is None:
            print(file)
        if trackno is None:
            trackno = 0
        for char in ["/","\\",":","?","<",'"',">","|","*"]:
             if title is not None:
                if char in title:
                    title = title.replace(char,"")
        if title is not None:
            separator = "/"
            filepath = separator.join((file.split("/")[0:len(file.split("/"))-1]))
            try:
                os.rename(file,f"{filepath}/{trackno} - {title}.mp3")
            except:
                os.rename(file,f"{filepath}/{trackno} - {title} DUPLICATE.mp3")
                # os.rename(file,f"{trackno} - {title}.mp3")




