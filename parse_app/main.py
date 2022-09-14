from bs4 import BeautifulSoup as BS
import time
import os


from pull_data import get_html, get_content, lookup_next
from settings import headers, bot_token, chat_id, chanel
from telegram_send import send_dump_to_telegram


def main(headers):
    page = 1
    while True:

        url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{}/c37l1700273'.format(page)
        html = get_html(url, headers)
        soup = BS(html.text, 'html.parser')
        get_content(soup)
        if not lookup_next(soup):
            os.system("sh make_dump.sh")
            print(f'[INFO] Sending dump file to telegram chanel {chanel}')
            time.sleep(5)
            
            send_dump_to_telegram(bot_token, chat_id, 'dump.real_estate.gz')
            print('[INFO] Done!')        

            break
        page += 1
        print(f'[INFO] Loading page={page}...')
        time.sleep(5)


main(headers)




