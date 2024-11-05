import common.get_dbTable as get_dbTable
import common.sql as sql_util

def get_shopee_order(puid=1691277887002530119):
    puid_dbTable = get_dbTable(puid)
    