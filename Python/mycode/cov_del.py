import os.path
import os
import xlwt
import sys
import glob

path="."

def txt2xls(fp,file):
    if os.path.exists(fp):
        print "doing",fp
        f=open(fp)
        wb=xlwt.Workbook()
        ws1 = wb.add_sheet("Sheet1")
        
        i=0
        for line in f.readlines():
                j=0
                for item in line.split('\t'):
                    try:
                        item=item.strip().decode('utf-8')
                    except UnicodeDecodeError:
                        print i,j,item
                        ws1.write(i,j,"NULL")
                    else:
                        ws1.write(i,j,item)
                    j=j+1
                i=i+1
        f.close() 
        wb.save(path+"\\dst\\"+str(file[:-4])+'.xls')
       # wb.save(os.path.dirname(f)+str(file[:-4])+'.xls')       

         

def getalltxtfilename2(path): 
    txtfilenames=[] 
    for dirpath,dirnames,filenames in os.walk(path): 
        filenames=filter(lambda filename:filename[-4:]=='.txt',filenames) 
        filenames=map(lambda filename:os.path.join(dirpath,filename),filenames) 
        txtfilenames.extend(filenames)
        #print filenames
    return txtfilenames
		
#def delline():	
for f in getalltxtfilename2('.'):
       #if '.txt' in f:
               lines = open(f).readlines()
               open(f, 'w').writelines(lines[1:])
               txt2xls(f,os.path.basename(f))

#def getfiles():
   # files=os.listdir(path+"\\src")
   # for file in files:
   # fp = path+"\\src\\"+file
   # txt2xls(fp,file)
   
for file in getalltxtfilename2('.'):
       fp = path+"\\src\\"+file
       txt2xls(fp,file)

if __name__=='__main__':
    #delline()
    #getfiles()
    print "done!"
    #raw_input()