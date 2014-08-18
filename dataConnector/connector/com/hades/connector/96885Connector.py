# -*- coding: utf-8 -*-
import requests
import BeautifulSoup
import re

hostName = "http://www.56885.net/"
session = requests.session()
request = session.get(hostName + 'hy_add_list.asp?id=491')
content = BeautifulSoup.BeautifulSoup(request.content, fromEncoding="gb18030")
allArea = content.findAll("span", {"class": "find_select_textno"})
allArea = allArea + content.findAll("span", {"class": "find_select_textok"})

for area in allArea:
    request = session.get(hostName + area.a["href"])
    content = BeautifulSoup.BeautifulSoup(request.content, fromEncoding="gb18030")
    allDetails = content.findAll("a", {"target": "_blank"})
    for detail in allDetails:
        if detail.text == u"详细信息":
            request = session.get(hostName + detail["href"])
            content = BeautifulSoup.BeautifulSoup(request.content, fromEncoding="gb18030")
            table = content.findAll("table", {"bgcolor": "#fafafa"})[2]
            cargoStatus = table.findAll("tr")[0].findAll("td")[1].text
            print cargoStatus
            cargoName = table.findAll("tr")[1].findAll("td")[1].text
            print cargoName
            cargoWeight = table.findAll("tr")[2].findAll("td")[1].text
            print cargoWeight
            requireTruckType = table.findAll("tr")[3].findAll("td")[1].text
            print requireTruckType
            cityFrom = table.findAll("tr")[4].findAll("td")[1].text
            print cityFrom
            cityTo = table.findAll("tr")[5].findAll("td")[1].text
            print cityTo
            payType = table.findAll("tr")[6].findAll("td")[1].text
            print payType
            dateRange = table.findAll("tr")[7].findAll("td")[1].text.split(u'至')
            dateFrom = dateRange[0]
            dateTo = dateRange[1]
            print dateFrom
            print dateTo
            contacts = table.findAll("tr")[8].findAll("td")[1].text
            print contacts
            phoneNum = table.findAll("tr")[9].findAll("td")[1].text
            print phoneNum
            publishOrg = table.findAll("tr")[10].findAll("td")[1].text
            

