##documentation available at https://pypi.org/project/simple-settings/

bigchaindb_app_id = '9f9cbef4'
bigchaindb_app_key = 'c9017b4d69146e5d51d2a3da8a2f1c82'
bigchaindb_testnet_url = 'https://test.bigchaindb.com'


SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
 
   #'REQUIRED_SETTINGS': ('API_TOKEN', 'DB_USER'),
   # 'DYNAMIC_SETTINGS': {
   #     'backend': 'redis',
   #     'pattern': 'DYNAMIC_*',
   #     'auto_casting': True,
   #     'prefix': 'MYAPP_'
   # }
}



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'my_log.log',
            'maxBytes': 50 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'default'
        },
    },
    'loggers': {
        '': {
            'handlers': ['logfile'],
            'level': 'ERROR'
        },
        'my_project': {
            'level': 'INFO',
            'propagate': True,
        },
    }
}
