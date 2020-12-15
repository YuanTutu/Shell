#--coding:utf-8--
#使用方法是把这文件和图片文件放一个路径下（别有其他内容）然后执行，就可以转成bs64,生成一个1.txt文件，但每次好像都要删除一遍txt不然追加内容不一样，就很奇怪
import base64
import os
pwd = os.path.split(os.path.realpath(__file__))#获取当前路径和py文件自身的元组
#print(pwd)
work = list(pwd)#元组转成列表
#print(work)
workspace = work[0]#获取列表的第一个元素，也就是路径
#print(workspace)
filelist = os.walk(workspace)
for files in filelist:
    #print(files)
    filename = list(files)
    print(filename)
    truefile=filename[-1][0]
    print(truefile)

with open(r'{}\{}'.format(workspace,truefile), 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data),'utf-8')
    #print(encodestr)
with open(r'{}\1.txt'.format(workspace), 'w+') as f:
    f.write(encodestr)
    f.close