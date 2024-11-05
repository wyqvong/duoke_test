import pytest
import common.request_util as request_util
from configparser import ConfigParser

# @pytest.fixture(scope='session')
def get_token():
    login_url = "https://dk-test1.meiyunji.net/api/v1/user/userLoginV2"
    login_body = {"email":"testvip@lazada.sg","password":"+lykrBlAGizUeE3fbVlgSQ=="}
    login_req = request_util.SendRequest(url=login_url,method='post',body=login_body)
    res = login_req.send_request(content_type="application/x-www-form-urlencoded; charset=UTF-8")
    conf_dir = 'config/conf.ini'
    config = ConfigParser()
    config.read(conf_dir)
    config.set('token','token',res['data']['token'])
    with open('config/conf.ini','w') as conf:
        config.write(conf)
    # return res['data']['token']

if __name__ == '__main__':
    get_token()