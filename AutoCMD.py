import os
import sys

def GetInput():
    path=input('please input the path (till "activity"):')
    activity = os.listdir(path)
    peo=eval(input('input the people numbers:'))
    num=eval(input('input the video numbers:'))
    return activity,peo,num,path        #读取输入：动作名列表、拍摄人数、每人拍摄视频、路径

def CreateNewDir(dirs,peo,path):
    for i in range(len(dirs)):
        for j in range(peo):
            NewPath=path+'/data'+'/'+dirs[i]+'/p'+str(j+1)
            os.makedirs(NewPath)        #创建新的data件夹

def ToDoc(lis,peo,n):
    doc = open('out.txt','w')
    for i in range((len(lis))):
        for m in range(peo):
            for j in range(n):
                h=str(j+1)
<<<<<<< HEAD
                print('python src/run_video_output.py --video activity/{0}/p{1}/{2}.avi --output activity/data/{0}/p{1}/{2}.txt'.format(lis[i],m+1,h.zfill(2)),file=doc)
    doc.close()          #循环创建全部指令，输出至文件
=======
                print('python src/run_video_output.py --video {3}/{0}/p{1}/{2}.avi --output {3}/data/{0}/p{1}/{2}.txt'.format(lis[i],m+1,h.zfill(2),MFolder),file=doc)
    doc.close()          #循环
>>>>>>> f4a6b7aa0f98e4435dd74e7a942a265a147ea5d5

def ReadDoc():
    result=[]
    with open('out.txt','r') as f:
        for line in f.readlines():
            lines=line.strip('\n')
            result.append(lines)
    return result        #从文件中读入全部指令放入列表

ls,people,num,cata=GetInput()
CreateNewDir(ls,people,cata)
ToDoc(ls,people,num)
cmd=ReadDoc()

os.system('activate tfpose')
for i in range(len(cmd)):
    os.system(cmd[i])      #在cmd行依次运行全部指令
