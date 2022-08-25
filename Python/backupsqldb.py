import time
from shutil import copyfile

def backup():
    now = time.strftime('%y%m%d%H%M%S')
    source='D:\\UVSM\\resources\\app\\server\\sqlite.db'
    # target_file='D:\\sqldbbackup\\'+now+'sqlite.db'
    target_file='D:\\数据库备份\\'+now+'sqlite.db'
    copyfile(source,target_file)


if __name__ == '__main__':
    backup()