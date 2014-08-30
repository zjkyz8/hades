# -*- coding: utf-8 -*-
from __init__ import *


class WuLiuTianXiaConnector:
    hostName = "http://www.56885.net/"
    session = requests.session()

    def __init__(self):
        pass

    def get_html_content(self, url=''):
        request = self.session.get(self.hostName + url)
        content = BeautifulSoup.BeautifulSoup(request.content, fromEncoding="gb18030")
        return content

    def get_all_area(self):
        content = self.get_html_content('hy_add_list.asp?id=491')
        all_area = content.findAll("span", {"class": "find_select_textno"})
        all_area = all_area + content.findAll("span", {"class": "find_select_textok"})
        return all_area

    def fetch_data_and_save(self):
        all_area = self.get_all_area()

        for area in all_area:
            content = self.get_html_content(area.a["href"])
            all_details = content.findAll("a", {"target": "_blank"})
            for detail in all_details:
                if detail.text == u"详细信息":
                    content = self.get_html_content(detail['href'])
                    table = content.findAll("table", {"bgcolor": "#fafafa"})[2]
                    all_info = table.findAll("tr")
                    date_range = all_info[7].findAll("td")[1].text.split(u'至')
                    date_from = datetime.strptime(date_range[0].replace(u'年', ' ').replace(u'月', ' ')
                                                  .replace(u'日', ''), '%Y %m %d')
                    date_to = datetime.strptime(date_range[1].replace(u'年', ' ').replace(u'月', ' ')
                                                .replace(u'日', ''), '%Y %m %d')
                    if date_to < datetime.now():
                        continue

                    cargo_status = all_info[0].findAll("td")[1].text
                    cargo_name = all_info[1].findAll("td")[1].text
                    cargo_weight = all_info[2].findAll("td")[1].text.replace('吨', '').replace('(', '').replace(')', '')
                    require_truck_info = all_info[3].findAll("td")[1].text
                    city_from = all_info[4].findAll("td")[1].text
                    city_to = all_info[5].findAll("td")[1].text
                    pay_type = all_info[6].findAll("td")[1].text
                    contacts = all_info[8].findAll("td")[1].text
                    phone_num = all_info[9].findAll("td")[1].text

                    publish_org = all_info[10].findAll("td")[1].text
                    address = all_info[11].findAll("td")[1].text
                    cargo_detail = all_info[12].findAll("td")[1].text
                    existing_records = Record.query.filter(and_(Record.date_from == date_from,
                                                          Record.date_to == date_to,
                                                          Record.cargo_status == cargo_status,
                                                          Record.cargo_weight == cargo_weight,
                                                          Record.city_from == city_from,
                                                          Record.city_to == city_to,
                                                          Record.phone_num == phone_num,
                                                          Record.contacts == contacts)).all()
                    if len(existing_records) == 0:
                        print "new record created"
                        record = Record(cargo_name, cargo_weight, date_from,
                                    date_to, require_truck_info, city_from, city_to, contacts, phone_num,
                                    publish_org, address, cargo_status, cargo_detail, pay_type)
                        db_session.add(record)
                        db_session.commit()