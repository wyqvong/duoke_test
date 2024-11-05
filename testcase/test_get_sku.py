import pytest
import common.request_util as request_util


class TestSku(object):
    # @pytest.mark.parametrize("args",shopId,platform,messageItemIds)
    #获取sku列表
    def test_get_skulist(get_token,shopId="1691277888957450926",platform="lazada",messageItemIds="3673558046"):
        test_url = "https://app.tongpaidang.com/api/v1/dk/product/list"
        test_method = 'post'
        test_body = {"shopId":shopId,"platform":platform,"messageItemIds":messageItemIds,"pageSize":200,"pageNo":1}
        sendRequest = request_util.SendRequest(url=test_url, method=test_method, body=test_body, token=get_token)
        res = sendRequest.send_request()
        shop_list = res['data']['list']
        sku_list = []
        for i in shop_list:
            for s in i['items']:
                sku_list.append(s['itemSku'])
        print(sku_list)
        return sku_list

if __name__ == '__main__':
    testsku = TestSku()
    print(testsku.get_skulist())