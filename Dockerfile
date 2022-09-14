FROM python:3.9

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install netcat -y 
RUN apt-get install postgresql gcc python3-dev musl-dev -y

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /usr/src/app/


COPY . /usr/src/app/

RUN groupadd zxc
RUN useradd -m -g zxc zxc -p zxc
RUN usermod -aG zxc zxc

RUN poetry install

