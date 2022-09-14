# HOW TO USE APP

### There re 2 ways (with docker and manual)

### Manual commands

###### clone project and install poetry if u don't have it on your local machine

    $ git clone ...
    $ curl -sSL https://install.python-poetry.org | python3 -
    $ %APPDATA%\Python\Scripts
    # details on https://python-poetry.org/docs/

###### init environment and run app

    $ poetry init
    $ poetry run python parse_app/main.py

###### After finish script will create dump.gz file localy and send it to tg_canel
    https://t.me/storage_psql_dumps


### Docker commands