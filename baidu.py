import requests
import json
from bs4 import BeautifulSoup

global line
line=""

def baidu():
    # url = "https://talent.baidu.com/baidu/web/httpservice/getPostList?workPlace=0/4/7/9&recruitType=12&postType=&pageSize=10&curPage=1&keyWord=&_=1517456292113"
    # url2 = "https://talent.baidu.com/baidu/web/httpservice/getPostList?postType=&workPlace=0/4/7/9&recruitType=12&keyWord=&pageSize=10&curPage=4"
    temp = "https://talent.baidu.com/baidu/web/httpservice/getPostList?postType=&workPlace=0/4/7/9&recruitType=12&keyWord=&pageSize=10&curPage="

    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:57.0)'
    }
    items = []
    output = open('baidu.json', 'wb')

    i = 1
    while True:
        global line

        url = temp + str(i)
        resHTML = requests.get(url, headers=headers)
        # resHTML2 = requests.get(url2, headers=headers)



        text = resHTML.text
        # text2 = resHTML2.text

        unicodestr = json.loads(text)
        # if i>3:
        #     break
        if unicodestr['currentPage'] < i:
            break
        # unicodestr2 = json.loads(text2)

        items += unicodestr['postList']

        # items.insert(unicodestr['postList'])
        
        test = line.encode('utf-8')

        print("success" + str(i))
        i += 1

    line = json.dumps(items, ensure_ascii=False).strip()
    result=line.encode('utf-8')
    output.write(result)
    output.close()


if __name__ == '__main__':
    baidu()