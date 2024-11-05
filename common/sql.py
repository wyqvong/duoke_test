import pymysql
from configparser import ConfigParser

class Mysql:
    def __init__(self, operate_dbname:str, operate_tablename:str):
        self._operate_tablename = operate_tablename
        self._operate_dbname = operate_dbname
        try:
            test1 = self._get_sql_conf()
            self._conn = pymysql.connect(**test1) # 连接数据库，配置参数
            self._cursor = self._conn.cursor() # 创建一个游标，用来执行查询
            self._get_field() # 获取此表中的字段名
        except Exception as e:
            raise Exception(f"数据库连接失败！！！\n请检查表名、配置参数是否正确或检查本地数据库是否已启动！\n{e}")
    #获取数据库配置
    def _get_sql_conf(self):
        conf_dir = 'config/conf.ini'
        config = ConfigParser()
        config.read(conf_dir)
        db_conf = {
            "host": config.get('database','host'), #连接主机的ip
            "port": int(config.get('database','port')),   #连接主机的端口
            "user": config.get('database','user'), #本地数据库的用户名
            "password": config.get('database','password'), #本地数据库的密码
            "database": self._operate_dbname, #连接的数据库
        }
        return db_conf
    # 获取_conn对象
    def get_connect(self):
        return self._conn
    # 获取_cursor对象
    def get_cursor(self):
        return self._cursor
    # 获取此表中的字段名
    def _get_field(self):
        self._cursor.execute(f"select * from {self._operate_tablename}")
        self._desc = self._cursor.description
        self._field_ = []
        for field in self._desc:
            self._field_.append(field[0])
    # 执行sql语句
    def _sql(self,sql):
        try:
            self._cursor.execute(sql)  # 执行sql语句
            self._conn.commit() # 执行sql语句后，进行提交
            return True
        except Exception as e:
            self._conn.rollback()  # 执行sql语句失败，进行回滚
            return False
    # 插入数据
    def insert(self, *value):
        if not isinstance(value[0],tuple): raise Exception("要求传入的参数类型为tuple元组!!!")
        if len(value) == 1: value=value[0]
        else:value = str(value)[1:-1]
        sql = f"insert into {self._operate_tablename}({','.join(self._field_[1:])}) values {value}"
        if not self._sql(sql,f"{value}插入"):
            print("请检查每一条记录字段是否正确！！！")

    # 查询：通过puid查询n条数据并且排序
    def select_by_puid(self,puid:int,number=1,order="",tyep="esc",field="*"):
        if field != "*": field = ','.join(field)
        if order == "" :
            sql = f"select {field} from {self._operate_tablename} where puid={puid}"
        else:
            sql = f"select {field} from {self._operate_tablename} where puid={puid} order by {order} {tyep}"
        self._cursor.execute(sql)
        return self._cursor.fetchmany(number)
    
    # 当对象被销毁时，游标先关闭,连接后关闭
    def __del__(self):
        self._cursor.close()
        self._conn.close()

if __name__ == '__main__':
    dk_mysql_config_param = {
        "host": "10.200.1.37", #连接主机的ip
        "port": 3306,   #连接主机的端口
        "user": "root", #本地数据库的用户名
        "password": "Dxm123654", #本地数据库的密码
        "database": "pythondemo", #连接的数据库
        "charset": "utf8" #设置编码格式
    }
    tablename = "oderList"
    dk_mysql = Mysql(tablename)