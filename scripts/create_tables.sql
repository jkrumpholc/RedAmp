create table public.ip_ioc
(
    id      serial
        constraint ip_ioc_pk
            primary key,
    sources varchar(255) not null,
    data    varchar(255) not null
);

create table public.url_ioc
(
    id     serial
        constraint url_ioc_pk
            primary key,
    source varchar(255) not null,
    data   varchar(255) not null
);