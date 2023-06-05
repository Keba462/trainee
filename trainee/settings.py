"""
Django settings for trainee project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import configparser
import os
from pathlib import Path
import sys

from django.core.management.color import color_style

# from .logging import LOGGING
style = color_style()



APP_NAME = 'trainee'

ETC_DIR = os.path.join('/etc/', APP_NAME)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y^%ox%vwq$^-@r#n@9b526c=19l@g5g3_21^_^mip2atg(bt^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 2

DEFAULT_STUDY_SITE = ''

CONFIG_FILE = f'{APP_NAME}.ini'

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# EDC SMS configuration
BASE_API_URL = config['edc_sms']['base_api_url']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_q',
    'crispy_forms',
    'django_extensions',
    'django_crypto_fields.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_calendar.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'trainee.apps.EdcBaseAppConfig',
    'trainee.apps.EdcProtocolAppConfig',
    'trainee.apps.EdcFacilityAppConfig',
    'trainee.apps.EdcAppointmentAppConfig',
    'trainee.apps.EdcVisitTrackingAppConfig',
    'trainee.apps.EdcIdentifierAppConfig',
    'trainee.apps.EdcDataManagerAppConfig',
    'trainee.apps.EdcSenaiteInterfaceAppConfig',
    'trainee.apps.EdcMetadataAppConfig',
    'trainee.apps.EdcSmsAppConfig',
    'trainee_subject.apps.AppConfig',
    'trainee_dashboard.apps.AppConfig',
    'trainee_visit_schedule.apps.AppConfig',
    'trainee_reference.apps.AppConfig',
    'trainee_metadata_rules.apps.AppConfig',
    'trainee_labs.apps.AppConfig',
    'trainee_prn.apps.AppConfig',
    'trainee_export.apps.AppConfig',
    'trainee_reports.apps.AppConfig',
    'trainee_calendar.apps.AppConfig',
    'trainee.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'trainee.urls'

SENAITE_CONFIGURATION = {
    'OPTIONS': {
        'read_default_file': '/etc/edc_senaite_interface/senaite.conf',
    },
}

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

WSGI_APPLICATION = 'trainee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

REVIEWER_SITE_ID = 41

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEVICE_ID = '99'
DEVICE_ROLE = 'CentralServer'

PARENT_REFERENCE_MODEL1 = ''

PARENT_REFERENCE_MODEL2 = ''

COUNTRY = 'botswana'
COMMUNITIES = config['communities']

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

# dashboards
DASHBOARD_URL_NAMES = {
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'subject_listboard_url': 'trainee_dashboard:subject_listboard_url',
    'screening_listboard_url': 'trainee_dashboard:screening_listboard_url',
    'subject_dashboard_url': 'trainee_dashboard:subject_dashboard_url',
    'contact_listboard_url': 'edc_sms:contact_listboard_url',
    'senaite_result_listboard_url': 'trainee_dashboard:subject_result_listboard_url',
    'export_listboard_url': 'trainee_export:export_listboard_url',
    }

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template' : 'trainee/base.html',
    'dashboard_base_template': 'trainee/base.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
    'screening_listboard_template': 'trainee_dashboard/screening/listboard.html',
    'subject_listboard_template': 'trainee_dashboard/subject/listboard.html',
    'subject_dashboard_template': 'trainee_dashboard/subject/dashboard.html',
    'contact_listboard_template': 'edc_sms/listboard.html',
    'senaite_result_listboard_template': 'trainee_dashboard/result_listboard.html',
    'export_listboard_template': 'trainee_export/listboard.html',
    
    

}