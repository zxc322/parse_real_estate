# HOW TO USE APP

### There re 2 ways (with docker and manual)

### Manual commands

### This path assumes you have installed poetry and postgresql

###### clone project and install poetry if u don't have it on your local machine

    $ git clone ...



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

###### Postgers commands

    $ sudo -i -u postgres
    $ psql  
    $ CREATE database real_estate;
    $ CREATE user zxc with encrypted password 'zxc';
    $ grant all privileges on database real_estate to zxc;

###### init environment and run app

    $ poetry install
    $ poetry run python parse_app/main.py

###### After finish script will create dump.gz file localy and send it to tg_canel
    https://t.me/storage_psql_dumps


### Docker commands
