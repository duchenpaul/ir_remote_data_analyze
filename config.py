import toolkit_config

configDict = toolkit_config.read_config_general()


MYSQL_CONFIG = configDict['mysql database']
SQLITE_CONFIG = configDict['sqlite database']