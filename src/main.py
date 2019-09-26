# -*- encoding: utf-8 -*- #
__author__ = 'FeiZhang 81597228@qq.com'
__date__ = '2019-07-20'

from mysqlconn import MyConn
from settings import DB_CONFIG
from gendocx import gen_doc, doc_append_table


def main():
    """
    entry point
    :return:
    """
    try:
        my_conn = MyConn(DB_CONFIG)
        conn = my_conn.conn
        with conn.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tb_list = cursor.fetchall()
            doc = gen_doc('数据库表结构说明', 'FEIZHANG')
            for tb in tb_list:
                print(tb)
                tb_name = tb[0]
                cursor.execute("SHOW FULL FIELDS FROM {}".format(tb_name))
                # Field | Type | Collation | Null | Key | Default | Extra | Privileges | Comment
                tb_rs = cursor.fetchall()
                # get table comment info
                cursor.execute("SELECT table_comment FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='{}'\
                 AND table_name='{}'".format(DB_CONFIG['db'], tb_name))
                tb_comment = cursor.fetchone()[0]
                # print("列名", "数据类型", "Null", "Key", "Default", "栏位说明")
                # for r in tb_rs:
                #     print(r[0], r[1], r[3], r[4], r[5], r[8])
                doc_append_table(doc, tb_rs, tb_name, tb_comment)
            output_file_name = "outputdoc/{}.docx".format(DB_CONFIG['db'])
            with open(output_file_name, "w") as file:
                doc.save(output_file_name)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
