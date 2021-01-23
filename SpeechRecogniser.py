import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
import os, glob
from os import path
#set the folder to be the input
os.chdir("E:\\PythonGarbage\\Speechrecog\wavs")
directory = os.getcwd()
# Make the output file.
totalfiles = len(glob.glob("*.wav"))
counter = 1
for wavefile in glob.glob("*.wav"):
    counter = counter+1
    print(directory+wavefile)
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), directory+r"\\"+wavefile)
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    # recognize speech using Sphinx
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        text = None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text = None
    try:
        print(f"File {counter} of {totalfiles} of,  {text}")
        with open("results.txt","a") as textfile:
            textfile.write(wavefile + " had the text: " + text + "\n")
            textfile.close()
    except:
        a = 1
