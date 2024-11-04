import pytest

import common.request_util as request_util

# @pytest.mark.parametrize("args",shopId,platform,messageItemIds)
#获取sku列表
def get_skulist(shopId="1691277888957450926",platform="lazada",messageItemIds="3673558046"):
    test_url = "https://app.tongpaidang.com/api/v1/dk/product/list"
    test_method = 'post'
    test_body = {"shopId":shopId,"platform":platform,"messageItemIds":messageItemIds,"pageSize":200,"pageNo":1}
    sendRequest = request_util.SendRequest(url=test_url, method=test_method, body=test_body)
    res = sendRequest.send_request()
    shop_list = res['data']['list']
    sku_list = []
    for i in shop_list:
        for s in i['items']:
            sku_list.append(s['itemSku'])
    return sku_list

if __name__ == '__main__':
    print(get_skulist())