from connector.WuliutianxiaConnector import WuLiuTianXiaConnector
from connector.WuTongConnector import WuTongConnector
from dataConnector.com.hades.repository.mapper.base_mapper import init_db

__author__ = 'xinhuang'

init_db()

# wu_liu_tian_xia_connector = WuLiuTianXiaConnector()
# wu_liu_tian_xia_connector.fetch_data_and_save()

wu_tong_connector = WuTongConnector()
wu_tong_connector.fetch_data_and_save()
