import os
import xml.etree.ElementTree as ET

# from tkinter import filedialog
# from tkinter import *
# root = Tk()
# root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Dom\Desktop\HLD", title="Select file")


tree = ET.parse("E:\\Games\CONTROL - Ultimate Edition\data_packfiles\SoundbanksInfo.xml")
A = [] #list of file IDs
B = [] #list of file short paths.
C = []
root = tree.getroot()
for level1 in iter(root):
    A.append(level1)
    for level2 in iter(level1):
        A.append(level2)
        for level3 in iter(level2):
            A.append(level3)
            for level4 in iter(level3):
                A.append(level4)
for i in range(len(A)):
    if A[i].tag == "File":
        if A[i+2].tag =="Path":
            # print(f"File tag found at {i} position")
            new = A[i + 2].text.split("\\")[-1]
            original = A[i].get('Id')
            count = 0
            try:
                # print(f"about to rename {original}.wem to {new}")
                os.rename(f"E:\\Games\\CONTROL - Ultimate Edition\\data_packfiles\\ep100-000-generic\\soundbanks\\{original}.wem",f"E:\\Games\\CONTROL - Ultimate Edition\\data_packfiles\\ep100-000-generic\\soundbanks\\{new}")
                count = count+1
                print(f"Success {count}")
            except:
                fail = 0
# C = zip(A,B)
#
# for file in os.listdir("E:\\Games\\CONTROL - Ultimate Edition\\data_packfiles\\ep100-000-generic\\soundbanks\\"):
#     if file in A:
#         print(file)
#     if file in B:
#         print(file)