# HOW TO USE APP

### There are 2 ways (with docker and manual)

### Manual commands
### This path assumes you have installed poetry and postgresql
###### clone project and install poetry if u don't have it on your local machine

    $ git clone https://github.com/zxc322/parse_real_estate.git


###### Create user with the same name as postgeres user ( it needed to run dump_psql script)

    $ sudo adduser zxc 
    $ sudo usermod -aG sudo zxc
    $ su zxc

###### Change const 'USE_DOCKER' to 'False' in parse_app/settings.py ( Default=True)


###### Create database (postgresql)
###### In my case db_name=real_estate, db_user=zxc, db_pass=zxc, db_host=localhost
###### You always can change it in parse_app/settings.py

    postgresql = {
    'pguser': 'zxc',
    'pgpswd': 'zxc',
    'pghost': 'localhost',
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
### This path assumes you have installed docker and docker-compose


###### clone project and install poetry if u don't have it on your local machine

    $ git clone https://github.com/zxc322/parse_real_estate.git
    
###### From directory wirh 'docker-compose.yml' run:

    $ docker-compose up --build
    
###### This command will start pulling data from source.It taked about 10 minutes. If u run w\o -d prefix logs let you know when process is done
###### When its done you can dump postgers data from docker (but container with db must be runing)

    # dump data
    $ docker exec postgres_db pg_dump -U zxc -F t real_estate | gzip > docker_real_estate.gz
    # send dump.gz to telegram chanel
    $ python send_dump_to_telegram.py

