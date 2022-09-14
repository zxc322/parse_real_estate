# HOW TO USE APP

### There re 2 ways (with docker and manual)

### Manual commands

###### clone project and install poetry if u don't have it on your local machine

    $ git clone ...
    $ curl -sSL https://install.python-poetry.org | python3 -
    $ %APPDATA%\Python\Scripts
    # details on https://python-poetry.org/docs/


###### Create database (postgresql)

###### In my case db_name=real_estate, db_user=zxc, db_pass=zxc, db_host=localhost
###### You always can change it in parse_app/settings.py

    postgresql = {
    'pguser': 'zxc',
    'pgpswd': 'zxc',
    'pghost': 'localhost', # set as 'db' for docker
    'pgport': 5432,
    'pgdb': 'real_estate'
    }

###### init environment and run app

    $ poetry init
    $ poetry run python parse_app/main.py

###### After finish script will create dump.gz file localy and send it to tg_canel
    https://t.me/storage_psql_dumps


### Docker commands