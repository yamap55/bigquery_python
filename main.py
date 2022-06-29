"""main"""
from logging import config, getLogger
from time import sleep

from google.cloud import bigquery

SQL_LIST = (
    "./sql/sample1.sql",
    "./sql/sample2.sql",
)


def main() -> None:
    """
    SQLファイルを実行する
    """
    logger = getLogger(__name__)

    client = bigquery.Client()
    for sql_path in SQL_LIST:
        logger.info("read sql")
        query = read_sql_file(sql_path)

        logger.info("execute sql")
        client.query(query)
        sleep(1)

    sleep(5)

    select_query = """
        SELECT _id, c1 FROM `bigquery-test-354810.dataset001.hoge` order by _id
    """
    query_job = client.query(select_query)

    logger.info("The query data")
    for row in query_job:
        logger.info(f'{row["_id"]}, {row["c1"]}')


def read_sql_file(sql_path: str) -> str:
    """
    SQLファイルを読み込む

    Parameters
    ----------
    sql_path : str
        SQLファイルのPATH

    Returns
    -------
    str
       SQLファイルの内容
    """
    with open(sql_path) as f:
        return f.read()


if __name__ == "__main__":
    config.fileConfig("logging.conf", disable_existing_loggers=False)
    main()
