import requests
from bs4 import BeautifulSoup
import fake_useragent

def Parser():
    url = 'https://kakoysegodnyaprazdnik.ru/baza/'
    user = fake_useragent.UserAgent().random
    headers = {
        'user-agent': user
    }
    responce = requests.get(url = url, headers = headers)
    responce.encoding = 'utf8'
    soup = BeautifulSoup(responce.text, 'xml')
    block = soup.find('div', class_ = 'wrap').find_all('div')[1]
    all_month = block.find_all('div', class_ = 'kalend_month')
    for month in all_month:
        month = month.find('div').find_all('div', class_ = 'baza-tooltip kalend_sun')
        for day in month:
            day = day.get('data-tooltip')
            day = day.replace(' Января', '.01').replace(' Февраля', '.02').replace(' Марта', '.03').replace(' Апреля', '.04').replace(' Мая', '.05').replace(' Июня', '.06').replace(' Июля', '.07').replace(' Августа', '.08').replace(' Сентября', '.09').replace(' Октября', '.10').replace(' Ноября', '.11').replace(' Декабря', '.12')
            print(day)
            with open('datas.txt', 'a') as f:
                f.write(f'{day}\n')
                f.close()



if __name__=='__main__':
    Parser()
