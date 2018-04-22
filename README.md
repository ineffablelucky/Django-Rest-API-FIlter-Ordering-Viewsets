# Django-Restful-API-Filter-Ordering-Viewsets

in you settings.py:
INSTALLED APPS:
..
..
'dataAPIapp',
'rest_framework',
'django_filters',
.
.

REST_FRAMEWORK = {

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    
    'PAGE_SIZE': 20,
    
    'limit' : 5,
    
    'DEFAULT_FILTER_BACKENDS': (
    
        'django_filters.rest_framework.DjangoFilterBackend',
        
    ),
    
    'ORDERING_PARAM' : 'sort',
    
}

To upload sampledata.json in your database (Postgresql recommended), run this command:
python manage.py importdata --path="path/to/sampledata.json"

for attaching databases: use this link 
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
