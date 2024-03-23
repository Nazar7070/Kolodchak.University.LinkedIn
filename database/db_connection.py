DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'linkediin.database.windows.net.database.windows.net',
        'NAME': 'LinkedIn',
        'USER': 'LinkedIn-admin',
        'PASSWORD': 'Kolodchak_07',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
