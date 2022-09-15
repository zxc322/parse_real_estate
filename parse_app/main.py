from bs4 import BeautifulSoup as BS
import time
import os

from settings import headers, bot_token, chat_id, chanel, USE_DOCKER

if USE_DOCKER:
    print('[INFO] Waiting for db creating...')
    time.sleep(5)
from pull_data import get_html, get_content, lookup_next
from telegram_send import send_dump_to_telegram




def main(headers):
    page = 1
    while True:

        url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{}/c37l1700273'.format(page)
        html = get_html(url, headers)
        soup = BS(html.text, 'html.parser')
        get_content(soup)

        if not lookup_next(soup):
            if USE_DOCKER:
                print('[INFO] Done!')
                print('[INFO] You can dump data by runing \n'
                '"docker exec postgres_db pg_dump -U zxc -F t real_estate | gzip > docker_real_estate.gz"')

                break
            else:
                os.system("sh make_dump.sh")                
                print(f'[INFO] Sending dump file to telegram chanel {chanel}')
                time.sleep(2)               
                send_dump_to_telegram(bot_token, chat_id, 'dump.real_estate.gz')
                print('[INFO] Done!')        
                break
        page += 1
        print(f'[INFO] Loading page={page}...')
        time.sleep(5)


if __name__=='__main__':
    main(headers)




