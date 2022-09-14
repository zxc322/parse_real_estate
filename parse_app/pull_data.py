import requests

from convert_date import get_correct_date
from database import insert_data_into_db



def get_html(url, headers):
    response = requests.get(url, headers)
    return response


def get_image(card):
    img_box = card.find('div', class_='left-col').find('div', class_='image')
    img = img_box.find('picture')
    try:
        image = img.find('source').get('data-srcset')
    except AttributeError:
        image = 'null'
    return image

def get_title(info_box):
    title = info_box.find('div', 'title').get_text(strip=True)    
    return title

def get_location(info_box):
    title = info_box.find('div', 'location').find('span').get_text(strip=True)    
    return title

def get_posted_date(info_box):
    posted = info_box.find('div', 'location').find('span', class_='date-posted').get_text(strip=True) 
    return get_correct_date(posted)

def get_bathrooms(card):
    bedrooms = card.find('div', class_='rental-info').find('span', class_='bedrooms').get_text(strip=True)
    beds = bedrooms.replace('\n', '').replace(' ', '')
    return beds

def get_description(info_box):
    description = info_box.find('div', class_='description').get_text(strip=True)
    return description

def get_price(info_box):
    full_price = info_box.find('div', class_='price').get_text(strip=True)
    if full_price[0].isalpha():        
        return (None, full_price)
    currency = full_price[0]
    price = full_price[1:]
    return (currency, price)
    

def lookup_next(soup):
    bottom_bar = soup.find('div', class_='bottom-bar')
    next = bottom_bar.find('div', 'pagination').find(title='Next')
    return next

def get_content(soup):
    items = soup.find_all('div', class_='search-item')

    for el in items:
        card = el.find('div', class_='clearfix')
        info_box = card.find('div', class_='info').find('div', class_='info-container')
        data = {
            'image': get_image(card),
            'title': get_title(info_box),
            'location': get_location(info_box),
            'published_date': get_posted_date(info_box),
            'bedrooms': get_bathrooms(card),
            'description': get_description(info_box),
            'full_price': get_price(info_box)
        }

        insert_data_into_db(data)