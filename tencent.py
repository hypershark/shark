from bs4 import BeautifulSoup

import requests
import json  #使用json格式存储


def tencent():
    temp = "https://hr.tencent.com/position.php?&start="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0)'
    }

    i=0
    items=[]
    while True:

        tmp = []
        url=temp+str(i*10)
        resHtml = requests.get(url, headers=headers)
        output = open('tencent.json', 'wb')
        html = BeautifulSoup(resHtml.text, 'html.parser')

        #创建CSS选择器
        result = html.select('tr[class="even"]')
        result2 = html.select('tr[class="odd"]')
        result += result2

        for site in result:
            item = {}

            name = site.select('td a')[0].get_text()
            dataLink = site.select('td a')[0].attrs['href']
            catalog = site.select('td')[1].get_text()
            recruitNumber = site.select('td')[2].get_text()
            workLocation = site.select('td')[3].get_text()
            publishTime = site.select('td')[4].get_text()

            item['name'] = name
            item['datailLink'] = url + dataLink
            item['catalog'] = catalog
            item['recruitNumber'] = recruitNumber
            item['publishTime'] = publishTime

            tmp.append(item)

        items+=tmp
        pagenav=html.select('div[class="pagenav"] a')
        t=len(pagenav)
        count=pagenav[len(pagenav)-2].get_text()
        if int(count)<(i*10):
            print(count)
            break

        print("success"+str(i))
        i+=1
    #禁用ascii编码，按utf-8编码
    line = json.dumps(items, ensure_ascii=False)

    test = line.encode('utf-8')
    output.write(test)

    output.close()


if __name__ == '__main__':
    tencent()