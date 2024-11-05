import pytest
from service.get_product import get_product_total
from common.excel_util import read_excel


class TestSku(object):
    @pytest.mark.parametrize("args",read_excel('testdata/sku.xlsx'))
    #获取sku列表
    def test_search_product(self,args):
        p_total = get_product_total(args["shopId"],args["平台"],args["搜索类型"],args["搜索文本"])
        print(p_total)
        assert p_total == args["预期总条数"]
        
if __name__ == '__main__':
    testsku = TestSku()
    print(testsku.test_search_product())