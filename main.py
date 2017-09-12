import requests
import time
import os
from bs4 import BeautifulSoup

def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    tbody = soup.find_all('tbody')[2]
    tr = tbody.find_all('tr')[1]
    data = [item.text for item in tr.find_all('td')]
    title = soup.b.text[:7]
    data[0] = '\t    ' + data[0]
    return title, data

def main(url):
    count = 0
    prevData = ['' * 6]
    while True:
        try:
            title, data = get_price(url)
            if data[0] != prevData[0]:
                if count % 20 == 0:
                    _ = os.system('clear')
                    print('\t'.join([title, '\b\btime', 'buy', 'sell', 'deal', '+-', 'quant']))
                print('\t'.join(data))
                prevData = data
                count += 1
            time.sleep(5)
        except KeyboardInterrupt:
            print('Bye')
            break
        except Exception as e:
            print('Stock Not Found')
            break

if __name__ == '__main__':
    sid = input('stock id: ')
    url = 'https://tw.stock.yahoo.com/q/ts?s=' + sid.strip()
    main(url)
