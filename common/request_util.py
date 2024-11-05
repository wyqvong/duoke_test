"""
统一封装request请求,提取host、headers公共部分
"""
import requests


class SendRequest:

    def __init__(self, url, method, body, token=None):
        """
        url:不带host的url地址 ,必填参数
        method:请求方法如 get、post、delete ,必填参数
        body:请求参数,字典格式 ,必填参数
        """
        self._url = url
        self._method = method
        self._body = body
        self._token = token

    #发送请求
    def send_request(self, content_type="application/json"):
        response = None
        headers = {"Content-Type": content_type, "Cookie": self._token}
        if self._method.upper() == "POST" and content_type == "application/json":
            response = requests.post(url=self._url, json=self._body, headers=headers)
        elif self._method.upper() == "POST" and content_type == "application/x-www-form-urlencoded; charset=UTF-8":
            response = requests.post(url=self._url, data=self._body, headers=headers)
        elif self._method.upper() == "GET":
            response = requests.get(url=self._url, params=self._body, headers=headers)
        else:
            print('请求方式与预期不符')
        return response.json()
    
if __name__ == '__main__':
    test_url = "https://app.tongpaidang.com/api/v1/dk/product/list"
    test_method = 'post'
    test_body = {"shopId":"1691277888957450926","platform":"lazada","messageItemIds":"3673558046","pageSize":200,"pageNo":1}
    res = SendRequest(url=test_url, method=test_method, body=test_body).send_request()
    # print(res.json()['data']['list'])
    shop_list = res['data']['list']
    sku_list = []
    for i in shop_list:
        for s in i['items']:
            sku_list.append(s['itemSku'])
    print(sku_list)
