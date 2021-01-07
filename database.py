from config import get_conf
from pymysql.connections import Connection


class MySQL(Connection):
    def __init__(self):
        host = get_conf("data_host")
        user = get_conf("data_user")
        pwd = get_conf("data_pwd")
        db = get_conf("data_database")
        # db = "qqq"
        super(MySQL, self).__init__(host, user, pwd, db)

    def checkTable(self):
        pass

    def insert(self, title, url, context):
        sql = f"""INSERT INTO 网易新闻(标题,网址, 内容)VALUES ('{title}','{url}','{context}')"""
        cursor = self.cursor()
        try:
            cursor.execute(sql)
            self.commit()
        except Exception as e:
            print(e)
            self.rollback()


if __name__ == '__main__':
    crawDB = MySQL()
    crawDB.close()
