import zipfile
import os
import random
import string
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
xdw = os.listdir("S:\Codingn't\decompiler.py\zip")
for i in range(len(xdw)):
    try:
        with zipfile.ZipFile("S:\Codingn't\decompiler.py\zip\\"+xdw[i],"r") as zip_ref:
            zip_ref.extractall("S:\RimWorld\Mods\\"+random_char(128))
        print("Finished")
    except:
        print("something broke terribly")