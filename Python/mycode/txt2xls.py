import os.path
import os
import xlwt
#仙剑rpg配置txt转换成xls

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


def getfiles():
    files=os.listdir(path+"\\src")
    for file in files:
        fp = path+"\\src\\"+file
        txt2xls(fp,file)

if __name__=='__main__':
    getfiles()
    print "done!"
    #raw_input()