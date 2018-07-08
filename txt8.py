import requests
import  os
from  lxml import  etree
#请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5383.400 QQBrowser/10.0.1313.400'}
#URL列表
urls=['https://www.ugirls.com/Content'.format(str(i)) for i in range(1, 2)]
#路径，可以更改成你的路径
path='D://小姐姐/大姐姐'
#获取图片并写入本地文件
def get_girlphoto(url):
    try:
        data = requests.get(url+"1", headers=headers)
        selector = etree.HTML(data.text)
        #获取图片的URL列表
        girlphoto_urls = selector.xpath('//div/a/img/@src')
        #循环每个图片链接并写入本地文件，写入要用二进制
        for item in girlphoto_urls:
            if not os.path.exists(path):
                os.makedirs(path)
                print("path创建成功")
            data = requests.get(item, headers=headers)
            with open(path + item[-7:], 'wb') as f:
                f.write(data.content)
                f.close()
    except :
        print("Exception")
if __name__ == '__main__':#主函数
    #循环URL
    for url in  urls:
        get_girlphoto(url)