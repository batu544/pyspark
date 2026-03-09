import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql') -> dict :
    """
    :param filename: contains database connection details
    :param section: section details inside the conf ini file
    :return: database dic
    """
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section('postgresql'):
        parms = parser.items(section)
        for parm in parms:
            db[parm[0]] = parm[1]
    else:
        raise Exception("No configuration found")
    return db


db = config()
print(db)

conn = psycopg2.connect(db)
