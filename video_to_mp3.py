# Converts the videos to mp3 
import os 
import subprocess

files = os.listdir("vd") 
for file in files: 
    tutorial_number = file.split(" [")[0].split(" #")[1]
    file_name = file.split(" ｜ ")[0]
    print( tutorial_number,  file_name)
    subprocess.run(["ffmpeg", "-i", f"vd/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])