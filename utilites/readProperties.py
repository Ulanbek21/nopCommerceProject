

#----------------Writ utiliti file which will read from ini file------
import sys
sys.path.append('.')
import configparser #Using this configparser call mthod RawConfigParser

config = configparser.RawConfigParser()# after creatin object creat config.read('.//Configurathion//config.ini')
config.read('.//Configuration//config.ini')


class ReadConfig:
    
    @staticmethod# this decoretor makes static
    def getApplicationURL():
        baseURL = config.get('common info','baseURL')
        return baseURL

    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password


