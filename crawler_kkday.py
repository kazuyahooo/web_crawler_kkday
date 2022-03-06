# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class KKDAY():
    def __init__(self, city):
        self.city = (5-len(city))*"0" + city

    def get_resp(self):
        headers = {'user-agent': ua.google}
        result = []
        # {'台北':'A01-001-00001', '台中':'A01-001-00002', '台南':'A01-001-00003', '高雄':'A01-001-00004', '花蓮':'A01-001-00005', '新北市':'A01-001-00006', '平溪':'A01-001-00007', '桃園':'A01-001-00008', '新竹':'A01-001-00009', '苗栗':'A01-001-00010', '彰化':'A01-001-00011', '南投':'A01-001-00012', '雲林':'A01-001-00013', '嘉義':'A01-001-00014', '屏東':'A01-001-00015', '墾丁':'A01-001-00016', '宜蘭':'A01-001-00017', '台東':'A01-001-00018', '澎湖':'A01-001-00019', '金門':'A01-001-00020', '馬祖':'A01-001-00021', '綠島':'A01-001-00023', '小琉球':'A01-001-00024', '蘭嶼':'A01-001-00025', '基隆':'A01-001-00026'}
        #url = "https://www.kkday.com/zh-tw/product/ajax_productlist/A01-001?city=A01-001-{self.city}&row=15&glang=&cat=&availstartdate=&availenddate=&fprice=&eprice=&sort=popularity&page=1"
        #url = "https://www.kkday.com/zh-tw/product/ajax_productlist/A01-001?city=A01-001-{self.city}&row=15&glang=&cat=TAG_2_1,TAG_2_2,TAG_2_3,TAG_2_4,TAG_2_6&availstartdate=&availenddate=&fprice=&eprice=&sort=popularity&page=1"
        url = f"https://www.kkday.com/zh-tw/product/ajax_productlist/A01-001?city=A01-001-{self.city}&row=15&glang=&cat=TAG_2_1,TAG_2_2,TAG_2_3,TAG_2_4,TAG_2_6&availstartdate=&availenddate=&fprice=&eprice=&sort=popularity&page=1"
        resp = requests.get(url, headers=headers)
        activities = resp.json()["data"]

        result = []
        for activity in activities:
            #result.append((activity["name"], activity["cities"]))
            if activity["cities"] not in result:
                result.append(activity["cities"])
        return result
        
        for activity in activities:
            # 票券名稱
            title = activity["name"]
            # 票券詳細內容連結
            link = activity["url"]
            # 票券價格
            price = activity["price"]
            # 最早可使用日期
            booking_date = activity["earliest_sale_date"]
            # 評價
            star = activity["rating_star"]	
            result.append(dict(title=title, link=link, price=price, booking_date=booking_date, star=star, source="KKday"))
        #print(result)
        return json.dumps(result, indent = 4, ensure_ascii=False)

ua = UserAgent(use_cache_server=False)
#kkday = KKDAY()
for i in range(1,50):
    present = KKDAY(str(i))
    print(present.get_resp(), present.city)
