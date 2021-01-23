import os, glob
os.chdir("E:\\Dom\\programs\Extractors\\WEM Og\\Python\\")
def trymakefolder(path):
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)
# Deal with all stray .wem files first
trymakefolder("outputs")
bnkname = "noparent"
for wem in glob.glob("*.wem"):
    try:
        wemname = wem.split(".")[0]
        print(f"renaming {wem} to {bnkname + wem}")
        os.rename(wem, bnkname + wem)
        os.system(f"ww2ogg.exe {bnkname + wem} --pcb packed_codebooks_aoTuV_603.bin") #ww2ogg .wem gives .ogg
        os.system(f"revorb.exe {bnkname + wemname}.ogg") #revorb .ogg gives .ogg
        os.system(f"del {bnkname + wem}")
        os.rename(bnkname + wemname + ".ogg", "outputs\\" + bnkname + "\\" + bnkname + wemname + ".ogg") #move each ogg into a folder per BNK
    except:
        print("didnt work lol")
# Now go through the bnks
for file in glob.glob("*bnk"):
    bnkname = file.split(".")[0]
    trymakefolder("outputs\\" + bnkname)
    os.system(f"bnkextr {file}")
    for wem in glob.glob("*.wem"):
        try:
            wemname = wem.split(".")[0]
            print(f"renaming {wem} to {bnkname + wem}")
            trymakefolder("outputs\\" + bnkname)
            os.rename(wem, bnkname + wem)
            os.system(f"ww2ogg.exe {bnkname + wem} --pcb packed_codebooks_aoTuV_603.bin") #ww2ogg .wem gives .ogg
            os.system(f"revorb.exe {bnkname + wemname}.ogg") #revorb .ogg gives .ogg
            os.system(f"del {bnkname + wem}")
            os.rename(bnkname + wemname + ".ogg", "outputs\\" + bnkname + "\\" + bnkname + wemname + ".ogg") #move each ogg into a folder per BNK
        except:
            print("didnt work lol")
os.system("del *.bnk")
