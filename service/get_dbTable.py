import common.request_util as request_util

def get_dbTable_by_puid(puid:int):
    url = "https://dk-test1-backend.meiyunji.net/util/getDbTable64"
    test_method = 'get'
    body = {"puid":puid}
    sendRequest = request_util.SendRequest(url=url,method=test_method,body=body)
    res = sendRequest.send_request()
    print(res)
    return res


if __name__ == '__main__':
    get_dbTable_by_puid(1691277887002530119)