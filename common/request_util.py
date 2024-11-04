"""
统一封装request请求,提取host、headers公共部分
"""
import requests


class SendRequest:

    def __init__(self, url, method, body):
        """
        url:不带host的url地址 ,必填参数
        method:请求方法如 get、post、delete ,必填参数
        body:请求参数,字典格式 ,必填参数
        """
        self._url = url
        self._method = method
        self._body = body
        self._token = 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2IjoxLCJpZCI6IjM5OTI2Njc4OTQzNjk0ODQ4MCIsImRhdGEiOnsidWlkIjoiMzk5MjY2Nzg5NDM2OTQ4NDgwIiwicHVpZCI6IjM5OTI2Njc4OTQzNjk0ODQ4MCIsImZ1bmN0aW9uYWxUZXN0Ijoid2hhdHNBcHAsc2hvcGlmeSxsaXZlY2hhdCxzZW5zaXRpdmVXb3JkLEltcG9ydGFudFRYLGFhYSxULVByZXZpZXcsc210YXV0aCxzZWFyY2hKTCxyZXR1cm5ERCxnZHNwLGFpb25kdXR5LG5vLXJlcGx5LG5ld3RyYW5zbGF0ZSxBSVZpZGVvLGxhemFkYVZvdWNoZXIsQnVsa0ZTLGdyb3VwQ2hhdE1ha2VvdmVyRm9yTGF6YWRhLGdyb3VwQ2hhdE1ha2VvdmVyRm9yU2hvcGVlLGdyb3VwQ2hhdE1ha2VvdmVyRm9yVGlrdG9rLGdyb3VwQ2hhdE1ha2VvdmVyRm9yVG9rb3BlZGlhLGdyb3VwQ2hhdE1ha2VvdmVyRm9yRGFyYXosZmxvdyx1bmlmZWRERCxBSW1hcmssVGlrVG9rVm91Y2hlcixpbnZpdGVmb2xsb3csU3RhdHVzUGVuZGluZyxUaWtUb2tSZXZlcnNlT3JkZXIsU2hvcGVlUmV2ZXJzZU9yZGVyIn0sImlhdCI6MTczMDAxMjg1MywiZXhwIjoyNDIxMjEyODUzfQ.H_N8rtFVsiVRyLxFeQEf2LUV6C5Zybdm9JLwPIPhcE8;'

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
