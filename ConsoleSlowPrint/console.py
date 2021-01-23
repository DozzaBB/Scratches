import os
import random
import time
#set the console colour
os.system('color 02')

def printinline(string):
    delay=30/1000 #this seems like a nice amount of delay
    n = random.randint(1,10)
    chunks = [string[i:i+n] for i in range(0, len(string), n)]
    for word in chunks:
        print(word,end="",flush=True)
        time.sleep(delay)
    print("")
while(1):
    with open("test.html",'r') as bible:
        for line in bible:
            printinline(line)
            if random.randint(1,10)==1:
                time.sleep(2)







