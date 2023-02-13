CREATE DATABASE icp_tasks_db;

CREATE USER icp_user WITH ENCRYPTED PASSWORD 'icp_u53r_p455';

ALTER ROLE icp_user SET client_encoding TO 'utf8';
ALTER ROLE icp_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE icp_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE icp_tasks_db TO icp_user;
GRANT USAGE, CREATE ON SCHEMA public TO icp_user;

