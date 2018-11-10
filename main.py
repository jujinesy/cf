import os
path = "E:\\0xFF\\0x06 기타\\18.11.05 n916s\\TPhone\\VoiceRecorder\\"
for file in os.listdir(path):
    all = file.split('.')
    filename = all[0].split('_')
    ext = all[1]
    os.rename(path+file, path+filename[2]+"_"+filename[1]+"_"+filename[3]+"_"+filename[4]+"_"+filename[5]+"."+ext)
