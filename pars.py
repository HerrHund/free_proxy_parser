import requests
from bs4 import BeautifulSoup
import json
from time import sleep
while True:
    def getProxy(url, name):
        
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        data = []
        table = soup.find('table', attrs={'class':'table table-striped table-bordered'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values

    
        with open(f'{name}.json', 'w') as fp:
            json.dump(data, fp)
        print(name + ' is done')

    getProxy('https://free-proxy-list.net/','free')
    getProxy('https://www.us-proxy.org/','us')
    getProxy('https://www.sslproxies.org/','ssl')
    getProxy('https://free-proxy-list.net/anonymous-proxy.html','anonymous')
    getProxy('https://www.socks-proxy.net/','socks')
    getProxy('https://free-proxy-list.net/uk-proxy.html','uk')

    sleep(600)