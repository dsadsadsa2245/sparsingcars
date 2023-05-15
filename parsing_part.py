from cars1 import Cars
import requests
from bs4 import BeautifulSoup
import lxml


def get_html(url):
    print("сбор html кода главной страницы...")
    """получаем html код с страницы,но он непонятный и внем нельзя сориентироваться"""
    # получаем непонятную кашу из html
    response = requests.get(url)
    return response.text


def get_soup(html):
    print("все еще сбор html")
    """делаем код более понятным"""
    # делаем html код более понятным
    soup = BeautifulSoup(html, 'lxml')
    return soup


def links(souphtml):
    """получаем ссылки каждой страницы, чтобы можно было проспарсить каждую отдельно"""
    a = souphtml.find_all('div', class_='list-item list-label')
    links = []
    for x in a:
        b = 'https://www.mashina.kg' + x.find('a').get('href')
        links.append(b)
    return links


def marks(souphtml):
    """получаем марки"""
    all_marks = souphtml.find_all('h2', class_='name')
    return all_marks


def year_color_engine_mileage():
    html = get_html('https://www.mashina.kg/search/all/')
    souphtml_ = get_soup(html)
    print("подождите пожалуйста,спарсинг начался...")
    pages = links(souphtml)
    z = 0
    for x in pages:
        html = get_html(x)
        souphtml_ = get_soup(html)
        our_block = souphtml_.find('div', class_='tab-pane').find_all('div', class_='field-row')
        marks_ = souphtml_.find('div', class_='details-breadcrumb').find_all('a')[2].get('href')[8:14].replace('/', '')
        model_ = souphtml_.find('div', class_='details-breadcrumb').find_all('a')[3].get('href').split('/')[3]
        price_ = souphtml_.find('div', class_='prices-block').find('div', class_='price-dollar').text
        year_ = souphtml_.find('div', class_='field-value').find('b').text
        mileage_ = our_block[1].find('b').text
        kuzov_ = our_block[2].find("div", class_="field-value").text
        color_ = our_block[3].find('div', class_='field-value').text
        engine_ = our_block[4].find('div', class_='field-value').text.strip()[0:4].replace('\n', '')
        a = Cars(marks_, model_, year_, engine_, color_, kuzov_, mileage_, price_, x).prepareforjson()
        z = z + 1
    b = Cars()
    b.send_to_json()
    # я создал новый элемент new_dict.Внутрь new_element() введите нужные параметры машины.Вставляйте эту переменную
    # в качестве аргумента там где необходим новый элемент,например update() принимает в себя новый элемент
    new_dict = b.new_element()
    # b.create(обязательно принимает в есбя пару аргументов, иначе вернет все значения None. добавляет его к списку машин)
    # b.listing(просто выводит вам список. не принимает аргументов)
    # b.retrieve(выводит вам один рандомный словарь из  списка)
    # b.update(нужно ввести индекс элемента котрый вы желаете заменить
    #b.update(5, new_dict)
    #b.delete(можно ввести либо "все",чтобы полностью очистить список.Или введите индекс)
    b.delete('все')


url = 'https://www.mashina.kg/search/all/'
html = get_html(url)
souphtml = get_soup(html)
"""ниже стоит код.Раскомментируйте его чтоюы запустить код.
Также с 59  строки можете проверить на работу миксины."""
year_color_engine_mileage()
