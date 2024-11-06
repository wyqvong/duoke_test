import os
from service.sql_select_shopee_order import select_shopee_order_by_puid
from service.get_product import get_skuList

def main():
    # tempdir = "output/reports/temp/%stemp" % time.strftime("%y%m%d-%H%M%S")
    os.system("pytest")
    print("使用封装好的requests请求testvip@lazada.sg账号的cb_MY店铺下获取商品列表数据并提取items字段中的itemSku值，以列表的形式返回")
    print('_______________________________________________________________________________________________________________')
    get_skuList("1691277887041120926","lazada")
    print("使用封装好的pymsql获取puid=1691277887002530119，shopee平台的订单表的订单编号、状态、买家名称、order_item内的variationSku字段值，创建时间倒序，前50条数据")
    print('_______________________________________________________________________________________________________________')
    select_shopee_order_by_puid(1691277887002530119)


if __name__ == '__main__':
    main()