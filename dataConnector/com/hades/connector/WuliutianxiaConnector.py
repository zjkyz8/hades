# -*- coding: utf-8 -*-

from datetime import datetime
from __init__ import *


class WuLiuTianXiaConnector:
    hostName = "http://www.56885.net/"
    session = requests.session()
    # record_repo =

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
                    date_range = table.findAll("tr")[7].findAll("td")[1].text.split(u'至')
                    date_from = datetime.strptime(date_range[0].replace(u'年', ' ').replace(u'月', ' ')
                                                  .replace(u'日', ''), '%Y %m %d')
                    date_to = datetime.strptime(date_range[1].replace(u'年', ' ').replace(u'月', ' ')
                                                .replace(u'日', ''), '%Y %m %d')
                    if date_to < datetime.now():
                        continue
                    print date_from
                    print date_to

                    cargo_status = table.findAll("tr")[0].findAll("td")[1].text
                    print cargo_status
                    cargo_name = table.findAll("tr")[1].findAll("td")[1].text
                    print cargo_name
                    cargo_weight = table.findAll("tr")[2].findAll("td")[1].text
                    print cargo_weight
                    require_truck_info = table.findAll("tr")[3].findAll("td")[1].text
                    print require_truck_info
                    city_from = table.findAll("tr")[4].findAll("td")[1].text
                    print city_from
                    city_to = table.findAll("tr")[5].findAll("td")[1].text
                    print city_to
                    pay_type = table.findAll("tr")[6].findAll("td")[1].text
                    print pay_type

                    contacts = table.findAll("tr")[8].findAll("td")[1].text
                    print contacts
                    phone_num = table.findAll("tr")[9].findAll("td")[1].text
                    print phone_num
                    publish_org = table.findAll("tr")[10].findAll("td")[1].text
                    print publish_org
                    address = table.findAll("tr")[11].findAll("td")[1].text
                    print address
                    cargo_detail = table.findAll("tr")[12].findAll("td")[1].text
                    print cargo_detail
                    print '---------------------------------'


