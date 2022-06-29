create table if not exists `bigquery-test-354810.dataset001.hoge` (
    _id STRING
    ,  c1 STRING
);

-- required wait.

insert into
`bigquery-test-354810.dataset001.hoge`
values("1", "a")
