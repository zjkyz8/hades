# -*- coding: utf-8 -*-

from __init__ import *


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

    def get_all_area(self):
        content = self.get_html_content('103.html?pid=2&f=&t=&lx=&hk=&hl=')
        all_area = content.findAll("span", {"class": "find_select_textno"})
        all_area = all_area + content.findAll("span", {"class": "find_select_textok"})
        return all_area

    def fetch_data_and_save(self):
        page_num = 100000
        while True:
            content = self.get_html_content('103.html?pid=' + `page_num` + '&f=&t=&lx=&hk=&hl=')
            error_msg = content.find("div", {
                "style": "float:left;width:450px;color:#333333;font-size:18px;font-weight:bold"})
            if error_msg.text == u"没有相关货源，您可查看相邻地区货源":
                print error_msg
                break

            print content
        # all_area = self.get_all_area()
        #
        # for area in all_area:
        # content = self.get_html_content(area.a["href"])
        #     all_details = content.findAll("a", {"target": "_blank"})
        #     for detail in all_details:
        #         if detail.text == u"详细信息":
        #             content = self.get_html_content(detail['href'])
        #             table = content.findAll("table", {"bgcolor": "#fafafa"})[2]
        #             date_range = table.findAll("tr")[7].findAll("td")[1].text.split(u'至')
        #             date_from = datetime.strptime(date_range[0].replace(u'年', ' ').replace(u'月', ' ')
        #                                           .replace(u'日', ''), '%Y %m %d')
        #             date_to = datetime.strptime(date_range[1].replace(u'年', ' ').replace(u'月', ' ')
        #                                         .replace(u'日', ''), '%Y %m %d')
        #             if date_to < datetime.now():
        #                 continue
        #             print date_from
        #             print date_to
        #
        #             cargo_status = table.findAll("tr")[0].findAll("td")[1].text
        #             print cargo_status
        #             cargo_name = table.findAll("tr")[1].findAll("td")[1].text
        #             print cargo_name
        #             cargo_weight = table.findAll("tr")[2].findAll("td")[1].text
        #             print cargo_weight
        #             require_truck_type = table.findAll("tr")[3].findAll("td")[1].text
        #             print require_truck_type
        #             city_from = table.findAll("tr")[4].findAll("td")[1].text
        #             print city_from
        #             city_to = table.findAll("tr")[5].findAll("td")[1].text
        #             print city_to
        #             pay_type = table.findAll("tr")[6].findAll("td")[1].text
        #             print pay_type
        #
        #             contacts = table.findAll("tr")[8].findAll("td")[1].text
        #             print contacts
        #             phone_num = table.findAll("tr")[9].findAll("td")[1].text
        #             print phone_num
        #             publish_org = table.findAll("tr")[10].findAll("td")[1].text
        #             print publish_org
        #             address = table.findAll("tr")[11].findAll("td")[1].text
        #             print address
        #             cargo_detail = table.findAll("tr")[12].findAll("td")[1].text
        #             print cargo_detail
        #             print '---------------------------------'


