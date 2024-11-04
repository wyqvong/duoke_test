import pymysql

class Mysql:
    def __init__(self, operate_tablename:str,my_sqldb_config_param:dict):
        self._operate_tablename = operate_tablename
        try:
            self._conn = pymysql.connect(**my_sqldb_config_param) # 连接数据库，配置参数
            self._cursor = self._conn.cursor() # 创建一个游标，用来执行查询
            self._get_field() # 获取此表中的字段名
        except Exception as e:
            raise Exception(f"数据库连接失败！！！\n请检查表名、配置参数是否正确或检查本地数据库是否已启动！\n{e}")
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
        if not isinstance(value[0],tuple): raise Exception("要求传入的参数类型为tuple元组！！！")
        if len(value) == 1: value=value[0]
        else:value = str(value)[1:-1]
        sql = f"insert into {self._operate_tablename}({','.join(self._field_[1:])}) values {value}"
        if not self._sql(sql,f"{value}插入"):
            print("请检查每一条记录字段是否正确！！！")
    # 查询：通过id查询一条数据
    def select_by_id(self,id_:int,field="*"):
        if field != "*": field = ','.join(field)
        sql = f"select {field} from {self._operate_tablename} where id={id_}"
        self._cursor.execute(sql)
        return self._cursor.fetchone()
    # 查询：指定查询多少条数数据,可根据简单条件查询（where 字段=”“）
    def select_many(self,num:int,query_builder=None,field="*"):
        if field != "*": field = ','.join(field)
        sql = f"select {field} from {self._operate_tablename}"
        if query_builder:
            if isinstance(query_builder,dict) and len(query_builder) == 1:
                query_builder = list(query_builder.items())[0]
                sql = f"select {field} from {self._operate_tablename} where {query_builder[0]}='{query_builder[1]}'"
            else: raise Exception("要求输入的条件为dict(字典)类型并且只能有一对键值（：len(dict）=1）！！！")
        self._cursor.execute(sql)
        return self._cursor.fetchmany(num)
    # 查询：所有数据
    def select_all(self, field="*"):
        if field != "*": field = ','.join(field)
        sql = f"select {field} from {self._operate_tablename}"
        self._cursor.execute(sql)
        return self._cursor.fetchall()
    # 查询：自定义sql语句查询数据
    def select_by_sql(self, sql):
        try:
            self._cursor.execute(sql)
            return self._cursor.fetchall()
        except Exception as e:
            print(f"数据查询失败！！！\n{e}")
    # 当对象被销毁时，游标先关闭,连接后关闭
    def __del__(self):
        self._cursor.close()
        self._conn.close()

if __name__ == '__main__':
    dk_mysql_config_param = {
        "host": "127.0.0.1", #连接主机的ip
        "port": 3306,   #连接主机的端口
        "user": "root", #本地数据库的用户名
        "password": "12345678", #本地数据库的密码
        "database": "pythondemo", #连接的数据库
        "charset": "utf8" #设置编码格式
    }
    tablename = "oderList"
    dk_mysql = Mysql(tablename, dk_mysql_config_param)