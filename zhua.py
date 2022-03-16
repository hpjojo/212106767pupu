import json
import threading
from datetime import time, datetime
from random import random
from time import strftime, localtime
from wsgiref import headers
#抓包过程
import requests
headers1={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
url='https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/dbe56a22-e58e-4e99-a2af-fab6e346f053'
resopnse = requests.get(url, headers=headers1).json()
print(resopnse)
#将json文件进行解析
def pupu(resopnse):
    # itme=json.dumps(resopnse)
    #
    # print(itme)

    # time1_str=datetime.datetime.now().strftime('%Y-%m-%d')
    name = resopnse['data']['name']
    d = resopnse['data']['price']
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    print(name,d/100)



def func_task():
    print('执行任务中...')
#定时器
def func_timer():

    func_task()
    global timer  # 定义全局变量
    # 定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
    timer = threading.Timer(10, func_timer)   # 10秒调用一次函数
    pupu(resopnse)


    timer.start()    #启用定时器

    timer = threading.Timer(1, func_timer)
# timer.start()
# print('定时器启动成功-----')



if __name__ == '__main__':
    func_timer()

