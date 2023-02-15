CREATE DATABASE icptasksdb;

CREATE USER icpuser WITH ENCRYPTED PASSWORD 'icp_u53r_p455';

ALTER ROLE icpuser SET client_encoding TO 'utf8';
ALTER ROLE icpuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE icpuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE icptasksdb TO icpuser;
GRANT USAGE, CREATE ON SCHEMA public TO icpuser;

