import toolkit_config
from sqlalchemy import create_engine

configDict = toolkit_config.read_config_general()


MYSQL_CONFIG = configDict['mysql database']
SQLITE_CONFIG = configDict['sqlite database']

IR_TRANSPONDER_URL = configDict['ir transponder']['url']

sqlite_engine = create_engine('sqlite:///{}'.format(SQLITE_CONFIG['db_file']), echo=False)

mysql_engine = create_engine(
    'mysql://{user}:{password}@{server}:{port}/{database}'.format(**MYSQL_CONFIG))