import requests
import json
from bs4 import BeautifulSoup


def wangyi():
    temp = "https://hr.163.com/position/list.do?currentPage="

    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:57.0)'
    }

    i = 1
    items=[]
    while True:

        tmp=[]
        url = temp + str(i)
        resHTML = requests.get(url, headers=headers)
        text = resHTML.text
        soup = BeautifulSoup(text, 'html.parser')
        [s.extract() for s in soup('span')]
        result = soup.select('tr')
        output = open('wangyi.json', 'wb')
        # print(result)

        j = 0
        for site in result:
            item = {}

            if (site.select('td') != [] and j % 2 == 1):
                name = site.select('td a')[0].get_text()
                dataLink = site.select('td a')[0].attrs['href']
                workType = site.select('td')[1].get_text()
                parttime = site.select('td')[2].get_text()
                workLocation = site.select('td')[3].get_text()
                recruitNumber = site.select('td')[4].get_text().strip()
                publishTime = site.select('td')[5].get_text()

                item['name'] = name
                item['dataLink'] = url + dataLink
                item['workType'] = workType
                item['parttime'] = parttime
                item['workLocation'] = workLocation
                item['recruitNumber'] = recruitNumber
                item['publishTime'] = publishTime

                items.append(item)
            j+=1
        items+=tmp

        i += 1
        print("sucess"+str(i))        
        count = soup.select('a[class=""]')[5].get_text()
        if int(count) < i:
            print(count)
            break

    line = json.dumps(items, ensure_ascii=False)

    test = line.encode('utf-8')
    output.write(test)

        # print(items)



if __name__ == '__main__':
    wangyi()