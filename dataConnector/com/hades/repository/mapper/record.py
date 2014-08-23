from __init__ import *
__author__ = 'xinhuang'


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True)
    cargo_name = Column(String(255))
    cargo_weight = Column(Float())
    cargo_status = Column(String(255))
    cargo_detail = Column(Text())

    date_from = Column(DateTime())
    date_to = Column(DateTime())
    require_truck_info = Column(String(255))
    city_from = Column(String(255))
    city_to = Column(String(255))
    pay_type = Column(String(255))

    contacts = Column(String(255))
    phone_num = Column(String(20))
    publish_org = Column(String(255))
    address = Column('address', Text())

    def __init__(self, cargo_name, cargo_weight, cargo_status, cargo_detail, date_from,
                 date_to, require_truck_info, city_from, city_to, pay_type, contacts, phone_num, publish_org, address):
        self.cargo_name = cargo_name
        self.cargo_weight = cargo_weight
        self.cargo_status = cargo_status
        self.cargo_detail = cargo_detail
        self.date_from = date_from
        self.date_to = date_to
        self.require_truck_info = require_truck_info
        self.city_from = city_from
        self.city_to = city_to
        self.pay_type = pay_type
        self.contacts = contacts
        self.phone_num = phone_num
        self.publish_org = publish_org
        self.address = address
