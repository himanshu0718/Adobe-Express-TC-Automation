import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','baseUrl')
        return url
        