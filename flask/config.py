import locale
import datetime

class Config(object):
    """
    Common configurations
    """

    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=3)
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}