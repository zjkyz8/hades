# -*- coding: utf-8 -*-
import time

from __init__ import *


def get_date_to(date_str):
    if date_str == u'长期货源':
        return datetime.max
    date_to = datetime.strptime(date_str, '%Y-%m-%d')
    return date_to


class WuTongConnector:
    host_name = "http://www.chinawutong.com/"

    def __init__(self):
        self.session = requests.session()
        pass

    def get_html_content(self, url=''):
        cookies = dict(UserInfo='87898C5F064DD214197764709A9EB119BF82532EDB53FDF4')
        headers = {"User-Agent":
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"}
        request = self.session.get(self.host_name + url, cookies=cookies, headers=headers)

        content = BeautifulSoup.BeautifulSoup(request.content, fromEncoding="gb18030")
        return content

    def fetch_data_and_save(self):
        page_num = 1
        while True:
            time.sleep(5)
            page_content = self.get_html_content('103.html?pid=' + `page_num` + '&f=&t=&lx=&hk=&hl=')
            error_msg = page_content.find("div", {
                "id": "ctl00_cphContent_noData",
                "style": "width:507px;height:50px;padding-top:20px;padding-left:120px;display:block;"})

            if error_msg is not None:
                break

            else:
                all_details = page_content.findAll("a", {"class": "fontsize14 fontweight"})
                for details in all_details:
                    page_content = self.get_html_content(details['href'])
                    detail_content = page_content.find("table", {"class": "mt10"}).findAll("tr")
                    date_from = datetime.today()
                    date_to = get_date_to(detail_content[5].findAll("td")[1].text)

                    if date_from > date_to:
                        continue

                    city_from = detail_content[0].findAll("td")[1].text
                    city_to = detail_content[1].findAll("td")[1].text
                    cargo_name = detail_content[2].findAll("td")[1].text
                    cargo_weight = detail_content[2].findAll("td")[3].text.replace(u'吨', '').replace('(', '').replace(
                        ')', '')
                    require_truck_info = detail_content[4].findAll("td")[1].text
                    contacts = detail_content[4].findAll("td")[3].text
                    phone_num = detail_content[5].findAll("td")[3].text
                    note = detail_content[6].findAll('td')[1].text + '\n' + detail_content[7].findAll('td')[1].text

                    publish_org_content = page_content.findAll("table", {"class": "mt10"})[1].findAll("tr")
                    publish_org = publish_org_content[0].findAll("td")[1].text
                    address = publish_org_content[3].findAll("td")[1].text

                    existing_records = Record.query.filter(and_(Record.date_to == date_to,
                                                                Record.cargo_weight == cargo_weight,
                                                                Record.city_from == city_from,
                                                                Record.city_to == city_to,
                                                                Record.phone_num == phone_num,
                                                                Record.contacts == contacts)).all()
                    if len(existing_records) == 0:
                        print "new record created"
                        record = Record(cargo_name, cargo_weight, date_from,
                                        date_to, require_truck_info, city_from, city_to, contacts, phone_num,
                                        publish_org, address, note)
                        db_session.add(record)
                        db_session.commit()

            page_num += 1