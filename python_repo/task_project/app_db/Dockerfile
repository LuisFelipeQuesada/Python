FROM postgres:15

ENV PATH $PATH:/usr/lib/postgresql/15/bin

RUN mkdir -p docker-entrypoint-initdb.d

WORKDIR /docker-entrypoint-initdb.d/
COPY init_db.sql /docker-entrypoint-initdb.d