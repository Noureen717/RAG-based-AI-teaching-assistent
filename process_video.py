# CONVERTS VIDEOS (mp4) INTO AUDIOS (mp3)

import os                                   #to read files from a folder
import subprocess                           #to run FFmpeg (audio extraction tool)
files = os.listdir("videos")                #returns all files inside the folder named as
for file in files:
    print(file)
    tutorial_number = file.split(" [")[0].split(" #")[1]
    file_name = file.split(" ｜ ")[0]
    print(tutorial_number,file_name)
    subprocess.run(["ffmpeg" , "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
    
    # -i --> input , It tells FFmpeg: “This is the file you should read from”
    # after -i we have input folder and then output folder.