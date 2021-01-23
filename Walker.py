path_abs =  "E:\Dom\programs\Extractors\Prey\star-citizen-texture-converter-v1-3\Extracted"
import os, shutil
walk = list(os.walk(path_abs))
for path, _, _ in walk[::-1]:
    if "poster" in path.lower():
        os.startfile(path)
    # if len(os.listdir(path)) == 0:
    #     os.rmdir(path)
    #     print(f"removed {path}")