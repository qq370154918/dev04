"""
Django settings for Dev04 project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 把某个路径添加到系统模块搜索路径中去
# sys.path为一个列表
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's+fn4*kowe8g_6$k9$3j2n(htf!w@dahdc!-iw4xi9xub@*411'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 可以使用哪些ip或者域名，来访问系统
# 默认为空，可以使用127.0.0.1或者localhost
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'drf_yasg',

    # 子应用名.apps.子应用名首字母大写Config
    # 'projects.apps.ProjectsConfig',
    'projects',
    'interfaces',
    'user',
    'testcases',
    'configures',
    'envs',
    'testsuits',
    'debugtalks',
    'reports',

    # 可以将某个目录（包）标记为Source Root，那么Pycharm会有智能提示
    # 不是Python的特性
    # 'apps.projects',
    # 'apps.interfaces'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 需要添加在CommonMiddleware中间件之前
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 4.添加白名单
# CORS_ORIGIN_ALLOW_ALL为True, 指定所有域名(ip)都可以访问后端接口, 默认为False
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST指定能够访问后端接口的ip或域名列表
# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:8080",
#     "http://localhost:8080",
#     "http://192.168.1.63:8080",
#     "http://127.0.0.1:9000",
#     "http://localhost:9000",
# ]

# 允许跨域时携带Cookie, 默认为False
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'Dev04.urls'

TEMPLATES = [
    {
        # a.指定模板引擎
        # b.常用的模板引擎，DjangoTemplates、Jinja2
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # c.指定html页面或者html模板存放的路径，可以添加多个路径
        # d.是Django搜索html页面或者html模板的路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # e.指定子应用下是否有html页面
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

WSGI_APPLICATION = 'Dev04.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# 1、需要在全局settings.py DATABASES字典中来配置数据的信息
DATABASES = {
    # 在Django数据库的标识
    'default': {
        # 指定数据库使用的引擎
        'ENGINE': 'django.db.backends.mysql',
        # 指定数据库的名称
        'NAME': 'dev04_dj',
        # 指定连接的数据库主机地址，域名和ip都可以
        'HOST' : '47.107.186.205',
        # 'HOST' : 'localhost',
        # 指定数据库的连接端口号，默认为3306,
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : '123456'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# 指定简体中文
LANGUAGE_CODE = 'zh-hans'
# 指定时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# 在全局配置文件settings.py文件中的REST_FRAMEWORK字典里修改DRF框架的配置
REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'errors',
    # a.可以修改默认的渲染类（处理返回的数据形式）
    'DEFAULT_RENDERER_CLASSES': [
        # b.列表中的元素是有优先级的，第一个元素优先级最高
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.backends.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
    # a.需要指定分页引擎，可以使用默认的PageNumberPagination分页引擎类
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.MyPagination',
    # b.必须指定每一页的数据条数
    'PAGE_SIZE': 3,

    # 指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # DEFAULT_AUTHENTICATION_CLASSES指定默认的认证类（认证方式）
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 指定使用JWT token认证方式
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 会话认证
        'rest_framework.authentication.SessionAuthentication',
        # 基本认证（用户名和密码认证）
        'rest_framework.authentication.BasicAuthentication',
    ],
    # DEFAULT_PERMISSION_CLASSES指定认证之后，能获取到的权限
    # 'DEFAULT_PERMISSION_CLASSES': [
        # AllowAny，不需要登陆就有任意权限
        # 'rest_framework.permissions.AllowAny',
        # IsAuthenticated只要登录之后，就具备任意权限
        # 'rest_framework.permissions.IsAuthenticated',
        # IsAdminUser指定只有为管理员用户才用任意权限
        # IsAuthenticatedOrReadOnly指定如果没登录，只能获取数据，如果登录成功，就具备任意权限
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # ],
}

# 可以在全局配置settings.py中的LOGGING，来配置日志信息
LOGGING = {
    # 版本号
    'version': 1,
    # 指定是否禁用已经存在的日志器
    'disable_existing_loggers': False,
    # 日志的显示格式
    'formatters': {
        # simple为简化版格式的日志
        'simple': {
            'format': '%(asctime)s - [%(levelname)s] - [msg]%(message)s'
        },
        # verbose为详细格式的日志
        'verbose': {
            'format': '%(asctime)s - [%(levelname)s] - %(name)s - [msg]%(message)s - [%(filename)s:%(lineno)d ]'
        },
    },
    # filters指定日志过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # handlers指定日志输出渠道
    'handlers': {
        # console指定输出到控制台
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 日志保存到日志文件
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            # 指定存放日志文件的所处路径
            'filename': os.path.join(BASE_DIR, "logs/test.log"),  # 日志文件的位置
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose',
            'encoding': 'utf-8'
        },
    },
    # 定义日志器
    'loggers': {
        'mytest': {  # 定义了一个名为mytest的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',  # 日志器接收的最低日志级别
        },
    }
}

# 默认使用的是Django auth子应用下的User模型类
# 可以指定自定义的模型类
# User模型类中有很多字段，其中有一个is_staff字段，指定是否为超级管理员，如果为0，这位普通用户
# 可以在命令下使用python manage.py createsuperuser，来创建超级管理员
# AUTH_USER_MODEL = 'auth.User'

# 在全局配置JWT_AUTH中，可以覆盖JWT相关的参数
JWT_AUTH = {
    # 指定处理登录接口响应数据的函数
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'utils.jwt_handle.jwt_response_payload_handler',

    # 前端用户访问一些需要认证之后的接口，那么默认需要在请求头中携带参数，
    # 请求key为Authorization，值为前缀 + 空格 + token值，如：JWT xxxssdhdsohsoshsohs

    # 可以指定token过期时间，默认为5分钟
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),

    # 指定前端传递token值的前缀
    # 'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}
