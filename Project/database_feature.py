import mysql.connector
from mysql.connector import errorcode
import check_features as cf
import json
import pandas as pd
import re
from datetime import datetime


def connect_sql(config):
    try:
        cnx = mysql.connector.connect(user=config['user'], password=config['password'],
                                      host=config['host'], port=config['port'])
        return cnx
    except mysql.connector.errorcode as err:
        print(err)
        return False


def connect_database(cnx, config):
    cursor = cnx.cursor()
    db = config['database']
    try:
        cursor.execute('USE {}'.format(db))
    except mysql.connector.Error as err:
        print('Database {} does not exists.'.format(db))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, db)
            print("Database {} create successfully.".format(db))
            cnx.database = db
        else:
            print(err)
            exit(1)


def create_database(cur, db_name):
    try:
        cur.execute("CREATE DATABASE {}".format(db_name))
    except mysql.connector.Error as err1:
        print("Failed creating database: {}".format(err1))
        exit(1)


def create_table(cur, name, info):
    try:
        print("Creating table {} ".format(name))
        cur.execute(info)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table is already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def update_by_id(cnx, table, label, value, id):
    try:
        sql = "UPDATE {} SET {} = '{}'".format(table, label[0], value[0])
        s_label = ''
        for i in range(1, len(label)):
            s_label += ", {} = '{}'".format(label[i], value[i])
        sql = sql + s_label + ' WHERE id = {}'.format(id)
        print(sql)
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def get_id(cursor, table_name, id):
    try:
        cursor.execute(f'select * from {table_name} where id = {id}')
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0


def delete_by_id(cnx, table_name, id):
    try:
        cursor = cnx.cursor()
        cursor.execute('delete from {} where id = {}'.format(table_name, id))
        cnx.commit()
        return 1
    except mysql.connector.Error as err:
        print(err)
        return 0


def insert_data(cnx, table, labels, data_input):
    try:
        sql = f'INSERT INTO {table} '
        label = '(' + labels[0]
        type_1 = '(' + '%s'
        for i in range(1, len(labels)):
            label += ',' + labels[i]
            type_1 += ',%s'
        label += ')'
        type_1 += ')'
        sql += label + ' VALUES ' + type_1
        cursor = cnx.cursor()
        cursor.execute(sql, data_input)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def show_table(cursor, table):
    try:
        cursor.execute(f'select * from {table}')
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def search_name(cursor, table, name):
    try:
        cursor.execute('select * from {} where name like \'%{}%\''.format(table, name))
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def retrive(cursor, table, num):
    try:
        cursor.execute('select * from {}'.format(table))
        results = cursor.fetchall()[-num:]
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def check_foreign_id(cursor, table_foreign, id):
    try:
        cursor.execute(f'select id from {table_foreign}')
        results = cursor.fetchall()
        id = int(id)
        for result in results:
            if id in result:
                return True
        return False
    except mysql.connector.Error as err:
        print(err)
    except:
        print('ID must be number: {}'.format(id))
    return False


def search_schedule(cursor, name, dateFrom, dateTo):
    try:
        cursor.execute(
            f'select * from schedule where name like \'%{name}%\' intersect select * from schedule  s where s.`date` > \'{dateFrom}\' and s.`date` < \'{dateTo}\'')
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(err)
    except:
        print('Fail')
    return False


def check_name(cursor, table, name):
    try:
        cursor.execute('select * from {} where name = \'{}\''.format(table, name))
        results = cursor.fetchone()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def export_data(table, data, label):
    try:
        df = pd.DataFrame(data=data, columns=label)
        filename = str(datetime.now())
        filename = re.sub("[-\s:]", '_', filename)
        filename = re.findall("[_\d]+", filename)
        filename = 'Output\\' + table + '_' + filename[0] + '.xlsx'
        df.to_excel(filename)
        return True
    except:
        print('Error')
        return False


if __name__ == "__main__":
    if cf.check_file_open('database_config.json'):
        with open('database_config.json') as f:
            config = json.load(f)
            f.close()
        cnx = connect_sql(config)
        cursor = cnx.cursor()
        connect_database(cnx, config)

        # table info

        table_hospital = "CREATE TABLE hospital (" \
                         "id INT auto_increment PRIMARY KEY," \
                         "name varchar(50) not null," \
                         "phone varchar(12) not null," \
                         "address varchar(200) not null," \
                         "description varchar(500))"

        table_doctor = "CREATE TABLE `doctor` (" \
                       "`id` int NOT NULL AUTO_INCREMENT," \
                       "`name` varchar(200) NOT NULL," \
                       "`phone` varchar(10) DEFAULT NULL," \
                       "`email` varchar(200) NOT NULL," \
                       "`address` varchar(200) NOT NULL," \
                       "`hospital_id` int NOT NULL," \
                       "PRIMARY KEY (`id`)," \
                       "KEY `doctor_FK` (`hospital_id`)," \
                       "CONSTRAINT `doctor_FK` FOREIGN KEY (`hospital_id`) REFERENCES `hospital` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT) ENGINE=InnoDB"

        table_patient = "CREATE TABLE `patient` (" \
                        "`id` int NOT NULL AUTO_INCREMENT," \
                        "`name` varchar(200) NOT NULL," \
                        "`phone` int NOT NULL," \
                        "`email` varchar(200) NOT NULL," \
                        "`address` varchar(200) NOT NULL," \
                        "`hospital_id` int NOT NULL," \
                        "PRIMARY KEY (`id`)," \
                        "KEY `patient_FK` (`hospital_id`)," \
                        "CONSTRAINT `patient_FK` FOREIGN KEY (`hospital_id`) REFERENCES `hospital` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT) ENGINE=InnoDB"

        table_schedule = "CREATE TABLE `schedule` (" \
                         "`id` int NOT NULL AUTO_INCREMENT," \
                         "`name` varchar(200) NOT NULL," \
                         "`date` datetime NOT NULL," \
                         "`doctor_id` int NOT NULL," \
                         "`patient_id` int NOT NULL," \
                         "`result` varchar(100) DEFAULT NULL," \
                         "PRIMARY KEY (`id`)," \
                         "KEY `schedule_FK` (`doctor_id`)," \
                         "KEY `schedule_FK_1` (`patient_id`)," \
                         "CONSTRAINT `schedule_FK` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT," \
                         "CONSTRAINT `schedule_FK_1` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT) ENGINE=InnoDB"

        """create_table(cursor,'hospital',table_hospital)
        create_table(cursor, 'doctor', table_doctor)
        create_table(cursor, 'patient', table_patient)
        create_table(cursor, 'schedule', table_schedule)"""
