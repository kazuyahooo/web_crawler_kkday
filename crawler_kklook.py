# -*- coding: utf-8 -*-
from email import header
import requests, json, csv, time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class KKLOOK():
    def __init__(self):
        pass
    def get_resp(self):
        headers = {'user-agent': ua.google, 'Accept-Language':'zh-TW'}
        result = []
        #url = f"https://www.klook.com/zh-TW/experiences/mcate/1-%e7%8e%a9%e6%a8%82/activity/?frontend_id_list=1&size=100"
        url = f"https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=1&size=24"
        resp = requests.get(url, headers=headers)
        total_page = resp.json()['result']['total'] // 100
        for each_page in range(1, total_page):
            if each_page != 1:
                url = f"https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=1&size=24&page={each_page}"
                resp = requests.get(url, headers=headers)
            activities = resp.json()["result"]['activities']
            self.collect_data(activities, result)
            time.sleep(10)
        return result

    def collect_data(self, activities, result):
        for activity in activities:
            title = activity['title']
            location_title = activity['location_title']
            deep_link = f"https://www.klook.com/{activity['deep_link']}"
            review_count = activity['review_hint'].split(' ')[0]
            review_join = activity['review_hint'].split(' ')[3]
            review_star = activity['review_star']
            sell_price = activity['sell_price']['amount_display']
            start_time = activity['start_time']
            what_we_love = activity['what_we_love']
            result.append(dict(title=title, location_title=location_title, deep_link=deep_link, review_count=review_count, review_join=review_join, review_star=review_star, sell_price=sell_price, start_time=start_time,what_we_love=what_we_love))

ua = UserAgent(use_cache_server=False)
total = list()
present = KKLOOK()
total = [elm for elm in present.get_resp() if elm not in total]
print("Crawler is done!")
try:
    with open('./data/kklook_output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=total[0].keys())
        writer.writeheader()
        for elm in total:
            writer.writerow(elm)
except IOError:
    print('Something went wrong with csv file!')
try:
    with open('./data/kklook_output.json', 'w', encoding='utf-8') as f:
        json.dump(total, f, indent = 4, ensure_ascii = False)
except IOError:
    print('Something went wrong with json file!')