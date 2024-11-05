from common.request_util import SendRequest
from configparser import ConfigParser

def get_skuList(shopId="1691277887041120926",platform="lazada",messageItemIds="3673558046"):
    test_url = "https://dk-test1.meiyunji.net/api/v1/dk/product/list"
    test_method = 'post'
    test_body = {"shopId":shopId,"platform":platform,"messageItemIds":messageItemIds,"pageSize":200,"pageNo":1}
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