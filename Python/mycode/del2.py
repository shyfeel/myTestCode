import os
import os.path
import sys
import glob

#仙剑rpg预处理，删除txt配置文件第一行
def getalltxtfilename2(path): 
    txtfilenames=[] 
    for dirpath,dirnames,filenames in os.walk(path): 
        filenames=filter(lambda filename:filename[-4:]=='.txt',filenames) 
        filenames=map(lambda filename:os.path.join(dirpath,filename),filenames) 
        txtfilenames.extend(filenames)
        #print filenames
    return txtfilenames

for f in getalltxtfilename2('.'):
       #if '.txt' in f:
               lines = open(f).readlines()
               open(f, 'w').writelines(lines[1:])