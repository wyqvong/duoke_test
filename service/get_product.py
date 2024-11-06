from common.request_util import SendRequest
from configparser import ConfigParser

def get_product_total(shopId,platform,searchField="",searchValue=""):
    test_url = "https://dk-test1.meiyunji.net/api/v1/dk/product/list"
    test_method = 'post'
    searchF = ""
    if searchField =="商品名":
        searchF = "platform_product_name"
    elif searchField == "商品ID":
        searchF = "platform_product_id"
    elif searchField == "SKU":
        searchF = "platform_product_sku"
    test_body = {"shopId":str(shopId),"platform":platform,"pageSize":200,"pageNo":1,"searchField":searchF,"searchValue":searchValue}
    print(test_body)
    config = ConfigParser()
    config.read('config/conf.ini')
    token = 'token='+config.get('token','token')
    sendRequest = SendRequest(url=test_url, method=test_method, body=test_body, token=token)
    res = sendRequest.send_request()
    return len(res['data']['list'])

def get_skuList(shopId="1691277887041120926",platform="lazada",searchField="",searchValue=""):
    test_url = "https://dk-test1.meiyunji.net/api/v1/dk/product/list"
    test_method = 'post'
    test_body = {"shopId":shopId,"platform":platform,"pageSize":200,"pageNo":1,"searchField":searchField,"searchValue":searchValue}
    config = ConfigParser()
    config.read('config/conf.ini')
    token = 'token='+config.get('token','token')
    sendRequest = SendRequest(url=test_url, method=test_method, body=test_body, token=token)
    res = sendRequest.send_request()
    shop_list = res['data']['list']
    sku_list = []
    for i in shop_list:
        for s in i['items']:
            sku_list.append(s['itemSku'])
    print(sku_list)
    return sku_list

if __name__ == '__main__':
    get_skuList()