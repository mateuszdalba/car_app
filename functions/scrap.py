#import bs4
from bs4 import BeautifulSoup4
    
import requests
import pandas as pd


def scrap_basic_info(url = 'https://www.otomoto.pl/osobowe', page=1):
    list_title = []
    list_link = []

    path = url + '?page=' + str(page)
    r = requests.get(path)
    soup = BeautifulSoup4(r.content, features="lxml")
    
    number_of_cars_on_page = len(soup.find_all('article'))
    
    for i in range(1,number_of_cars_on_page):
        tag = soup.find_all('article')[i]
        link = tag.find('a')['href']
        title = str(tag.find('a')).split('>')[1][:-3]
        
        if link == 'https://www.facebook.com/otomotopl' or link=='https://pomoc.otomoto.pl' or link == 'https://www.otomoto.pl/umowa-kupna-sprzedazy/' or link == 'https://pomoc.otomoto.pl/hc/pl/articles/216416787-Cennik-dla-Klient%C3%B3w-Indywidualnych' or link == 'https://otomotoklik.pl/?utm_source=otomoto&utm_medium=footer' or link == 'https://play.google.com/store/apps/details?id=pl.otomoto':
            continue
    
        list_title.append(title)
        list_link.append(link)

    df_basic = pd.DataFrame({'title':list_title, 'link':list_link})

    return df_basic


def make_line(main_features):
    featsFile = open('data/feats.txt', 'r', encoding="utf8")
    all_feats = featsFile.readlines()
    all_feats = [x.replace('\n','') for x in all_feats]
    temp = dict()
    for feat in all_feats:
        if feat not in main_features.keys():
             temp[feat] = None
        else:
            temp[feat] = main_features[feat]

    featsFile.close()

    return temp


def scrap_full_info(idx=0, basic_df=pd.DataFrame()):

    df_basic = basic_df
    
    title = df_basic.iloc[idx]['title']
    
    url = df_basic.iloc[idx]['link']
    r = requests.get(url)
    soup = BeautifulSoup4(r.content, features="lxml")
    #print(soup)
    
    #Main params
    params = soup.find_all(class_='offer-params__item')
    
    features = dict()
    
    for main_param in params:
        text = main_param.find('span', class_='offer-params__label').text.strip()
        label = main_param.find('a', class_='offer-params__link')
        if label == None:
            label = main_param.find('div', class_='offer-params__value')
        label = label.text.strip()
        features[text] = label
        
    #More params    
    params_2 = soup.find_all("li", class_='offer-features__item')
    
    for additional_param in params_2:
        features[additional_param.text.strip()] = 1
        
    price = soup.find('span', class_='offer-price__number').text.strip().split()[:-1]
    price = "".join(price)
    features['Cena'] = price
    
    currency = soup.find('span', class_='offer-price__currency').text.strip()
    features['Waluta'] = currency
    
    price_details = soup.find('span', class_='offer-price__details').text.strip()
    features['Szczegóły ceny'] = price_details
    
    description = soup.find('div', class_='offer-description__description').text.strip()
    features['Opis'] = description
    

    
    features = make_line(features)
    
    features['title'] = title
    features['link'] = url
    
    return features