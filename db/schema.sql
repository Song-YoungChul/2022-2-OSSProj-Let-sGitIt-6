-- drop table if exists user;

create table if not exists easy_mode (
    user_id integer primary key autoincrement,
    username string not null,
    score string not null
);

create table if not exists hard_mode (
    user_id integer primary key autoincrement,
    username string not null,
    score string not null
);

CREATE TABLE if NOT EXISTS item(
    id integer primary key autoincrement,
    name string not null,
    count integer not null default 0,
    price integer not null default 0
);


INSERT OR IGNORE INTO item (id, name, count, price) VALUES (2, 'life', 0, 30);
INSERT OR IGNORE INTO item (id, name, count, price) VALUES (3, 'slow', 0, 30);
INSERT OR IGNORE INTO item (id, name, count, price) VALUES (4, 'coin', 0, 30);

