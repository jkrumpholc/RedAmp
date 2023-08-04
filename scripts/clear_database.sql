DELETE FROM ip_ioc WHERE id > 0;
DELETE FROM url_ioc WHERE id > 0;
DELETE FROM sources WHERE url != '';
ALTER SEQUENCE ip_ioc_id_seq RESTART;
ALTER SEQUENCE url_ioc_id_seq RESTART;