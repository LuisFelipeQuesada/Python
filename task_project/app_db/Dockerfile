FROM mysql

RUN mkdir -p docker-entrypoint-initdb.d

WORKDIR /docker-entrypoint-initdb.d/
COPY init_db.sql /docker-entrypoint-initdb.d