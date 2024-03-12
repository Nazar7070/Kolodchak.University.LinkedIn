MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Додайте цей рядок
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'accounts',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'LinkedIn',  # додаток користувачів

]
ROOT_URLCONF = 'LinkedIn.urls'

SECRET_KEY = 'django-insecure-abcdef1234567890'

STATIC_URL = '/static/'

# Залиште цей рядок, щоб показати, що DEBUG встановлено як True
DEBUG = True

# Додайте ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Решта налаштувань...
