from common.sql import Mysql
from service.get_dbTable import get_dbTable_by_puid
import json

def select_shopee_order_by_puid(puid:int):
    db_table = get_dbTable_by_puid(puid)
    dk_mysql = Mysql("dk_backend__"+str(db_table['数据库']),"t_shopee_order__"+str(db_table['数据表']))
    order_sql_list = dk_mysql.select_by_puid(puid,50,"create_time","desc",["ordersn","order_status","buyer_username","order_item"])
    order_list = []
    for i in order_sql_list:
        order = {"订单编号":i[0],"状态":i[1],"买家名称":i[2],"SKU":[]}
        for s in json.loads(i[3]):
            order["SKU"].append(s["variationSku"])
        order_list.append(order)
    print(order_list)
        
if __name__ == '__main__':
    select_shopee_order_by_puid(1691277887002530119)


    