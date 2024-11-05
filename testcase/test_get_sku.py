import pytest
from service.get_sku import get_skuList


class TestSku(object):
    # @pytest.mark.parametrize("args",shopId,platform)
    #获取sku列表
    def test_search_product(shopId="1691277888957450926",platform="lazada"):
        get_skuList(shopId,platform)

if __name__ == '__main__':
    testsku = TestSku()
    print(testsku.get_skulist())