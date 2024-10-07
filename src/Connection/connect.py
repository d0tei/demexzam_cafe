from peewee import *


connect = MySQLDatabase ('SerT1234_cafe_demo',
                          user ='SerT1234_AdmCafe',
                          password = '9712',
                          host = '10.11.13.118',
                          port = 3306)



if __name__ == "__main__":
    connect.connect()