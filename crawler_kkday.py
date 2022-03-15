# -*- coding: utf-8 -*-
import requests, json, csv, time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

tags_file = open('./data/tags.json', 'r', encoding='utf-8').read()
cities_file = open('./data/cities.json', 'r', encoding='utf-8').read()
tags = json.loads(tags_file)
cities = json.loads(cities_file)

class KKDAY():
    # option: 1 > all countries, 2 > specified cities
    def __init__(self, city_num, option=1):
        self.city_num = city_num
        self.option = option

    def get_resp(self):
        headers = {'user-agent': ua.google}
        result = []
        city_code = '' if self.option == 1 else self.city_num
        url = f"https://www.kkday.com/zh-tw/product/ajax_productlist/?country=&city={city_code}&keyword=&availstartdate=&availenddate=&cat=&time=&glang=&sort=popularity&page=1&row=100&fprice=*&eprice=*&precurrency=TWD"
        resp = requests.get(url, headers=headers)
        for each_page in range(1, resp.json()['total_page']+1):
            if each_page != 1:
                url = f"https://www.kkday.com/zh-tw/product/ajax_productlist/?country=&city={city_code}&keyword=&availstartdate=&availenddate=&cat=&time=&glang=&sort=popularity&page={each_page}&row=100&fprice=*&eprice=*&precurrency=TWD"
                resp = requests.get(url, headers=headers)
            activities = resp.json()["data"]
            self.collect_data(activities, result)
            time.sleep(10)
        return result    

    def collect_data(self, activities, result):
            for activity in activities:
                if activity["sale_status"] == "0": # 已售罄 kkday排序已售罄全部放在後面
                    break
                else:
                    title = activity["name"] # 票券名稱
                    link = activity["url"] # 票券詳細內容連結
                    price = activity["price"] # 票券價格
                    booking_date = activity["earliest_sale_date"] # 最早可使用日期
                    rating_count = activity["rating_count"]	 # 評價人數
                    rating_star = activity["rating_star"] # 評價星級
                    country = activity["countries"][0]['name'] # 國家
                    cities = [elm['name'] for elm in activity["cities"]] # 城市
                    introduction = activity["introduction"].replace('\n','') # 介紹
                    cat_key = list(set([tags[elm] for elm in activity['cat_key']]))
                    result.append(dict(title=title, introduction=introduction, link=link, price=price, booking_date=booking_date, rating_star=rating_star, rating_count=rating_count,country = country, cities=cities,cat_key=cat_key))

ua = UserAgent(use_cache_server=False)
total = list()
present = KKDAY('all')
total = [elm for elm in present.get_resp() if elm not in total]
print("Crawler is done!")
try:
    with open('./data/output0315.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=total[0].keys())
        writer.writeheader()
        for elm in total:
            writer.writerow(elm)
except IOError:
    print('Something went wrong with csv file!')
try:
    with open('./data/output0315.json', 'w', encoding='utf-8') as f:
        json.dump(total, f, indent = 4, ensure_ascii = False)
except IOError:
    print('Something went wrong with json file!')