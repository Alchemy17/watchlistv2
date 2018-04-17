import os

class Config:
    '''
    Parent configuration class that will hold universal configurations
    for the project irregadless of the environment
    '''
    
    MOVIE_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_SEARCH_BASE_URL='https://api.themoviedb.org/3/search/movie?api_key={}&query={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration class that holds configurations for the production environment. It inherits the configuration properties of the config class

    Args:
        1. Config: Parent class with universal configuration
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration class that holds configurations for the Development environment. It inherits the configuration properties of the config class

    Args:
        1. Config: Parent class with universal configuration
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}