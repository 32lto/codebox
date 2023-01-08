import os
import environ
from pathlib import Path
from .settings_common import *

env = environ.Env(DEBUG=(bool,True))
env.read_env(os.path.join(BASE_DIR,'.env'))


# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
SECRET_KEY = env.get_value('DJANGO_SECRET_KEY',str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


#Static file location
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

LOGGING = {
    'version': 1, # １固定
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers': {
        #Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        #diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    #ハンドラの設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/opt/venv/codebox/Python_study/django_study/djst_diary/logs/django.log',
            'formatter': 'prod',
            'when': 'D', #ログローテーション間隔"日"
            'interval': 1,#ログローテーション間隔（1日）
            'backupCount': 7,
        },
    },

    #フォーマッタの設定
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

