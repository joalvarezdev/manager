import configparser
from dotenv import dotenv_values


def get_db_configuration() -> dict:
    return dict(config["DATA_SOURCE"])


def get_security_config() -> dict:
    return dict(config['SECURITY'])


environments = dotenv_values('.env')

config = configparser.ConfigParser()
config.read("config.ini")

config['SECURITY']: dict[str,str] | None = dict({"secret": environments['SECRET_KEY'], "algorithm": environments['ALGORITHM']})
