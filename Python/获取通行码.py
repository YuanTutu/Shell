# 为了朋友快捷工作获取excel内的健康码行程码等图片数据而编写
import xlrd
import requests
import logging

a = xlrd.open_workbook('D:/origin.xlsx', 'r')  # 打开.xlsx文件
sht = a.sheets()[0]  # 打开表格中第一个sheet
row1 = sht.row_values(1)

# 设置要下载的图片的范围，对应于 Excel 中的行数
start = 1
#获取excel
nrows = sht.nrows

for i in range(start, nrows):
    url = sht.cell(i, 7).value  # 依次读取每行第八列的行程码，也就是 URL
    if url:
        logging.info(url)
        # try:
        #     f = requests.get(url)
        # except:
        #     pass
        f = requests.get(url)
        roadName=sht.cell(i,0).value
        markNo=sht.cell(i, 3).value
        ii = str(roadName)+"_"+markNo  # 按照下载顺序（行号）构造文件名

        url2 = url[-3:]  # 根据链接地址获取文件后缀，后缀有.jpg 和 .gif 两种
        dir = ii + "." + url2  # 构造完整文件名称
        try:
            with open(dir, "wb") as code:
                code.write(f.content)  # 保存文件
            print(url)  # 打印当前的 URL
        except:
            pass

        jindu = (i - start) / (nrows - start) * 100  # 计算下载进度
        print("下载进度：", jindu, "%")  # 显示下载进度