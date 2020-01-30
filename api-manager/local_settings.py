import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Used internally by Django, can be anything of your choice
# {{ ansible_managed }}
SECRET_KEY = os.environ.get("OBP_MANAGER_SECRET_KEY", "yoursecretkey")
API_HOST = os.environ.get('OBP_MANAGER_API_HOST', 'http://127.0.0.1:8080')
API_BASE_PATH = os.environ.get('OBP_MANAGER_API_BASE_PATH', '/obp/v')
API_VERSION = os.environ.get('OBP_MANAGER_API_VERSION', '3.1.0')
OAUTH_CONSUMER_KEY = os.environ.get('OBP_MANAGER_OAUTH_CONSUMER_KEY', 'your_consumer_key')
#OAUTH_CONSUMER_KEY = 'your_consumer_key'
OAUTH_CONSUMER_SECRET = os.environ.get('OBP_MANAGER_OAUTH_CONSUMER_SECRET', 'your_consumer_secret')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', os.environ.get("OBP_MANAGER_ALLOWED_HOST")]
ADMINS = [
	('Admin', 'admin@tesobe.com')
]
SERVER_EMAIL = 'apimanager@apisandbox.openbankproject.com'
EMAIL_HOST = 'mail.tesobe.com'
EMAIL_USE_TLS = True
DEBUG = os.environ.get("OBP_MANAGER_DEBUG", True)
EXCLUDE_FUNCTIONS = ['getMetrics', 'getConnectorMetrics', 'getAggregateMetrics']
EXCLUDE_URL_PATTERN = ['%management/metrics%', '%management/aggregate-metrics%']
API_DATEFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', '..', 'db.sqlite3'),
    }
}
