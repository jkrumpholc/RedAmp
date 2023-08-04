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

create table public.sources
(
    url        varchar not null,
    ioc_type   varchar not null,
    from_index integer not null,
    to_index   integer not null
);

create sequence public.ip_ioc_id_seq
    as integer;
alter sequence public.ip_ioc_id_seq owned by public.ip_ioc.id;

create sequence public.url_ioc_id_seq
    as integer;
alter sequence public.url_ioc_id_seq owned by public.url_ioc.id;





