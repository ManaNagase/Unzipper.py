#imports
import zipfile
import os
import random
import string

#Your Variables
zip_folder = ""
output_folder = ""


#Function for random folder names
def random_char(r):
    return "".join(random.choice(string.ascii_letters) for i in range(r))

#Gets the zip folder
try:
    xdw = os.listdir(zip_folder)
except:
    print("You shouldn't be seeing this")
    #Really, If you Do Make A Pull Request Or Set Your Variables In Case You Haven't


for i in range(len(xdw)):
    try:
        #Unzip
        #I have no idea how i got this to work, so don't touch anything if you don't know what you're doing
        with zipfile.ZipFile(zip_folder+"\\"+xdw[i],"r") as zip_ref:
            zip_ref.extractall(output_folder+"\\"+random_char(128))
        print("Finished")
    except:
        print("You shouldn't be seeing this")
        #Really, If you Do Make A Pull Request Or Set Your Variables In Case You Haven't
