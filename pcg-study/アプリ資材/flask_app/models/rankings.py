from db import get_connection
import psycopg2
from psycopg2.extras import DictCursor

#get all mydata record
def getAll(game_name):
    # withはなぜか失敗したのでいつか原因調査・リトライ
    # with get_connection() as conn:
    #     with conn.cursor as cur:
    #         cur.execute('SELECT * FROM mydata')
    #         all_record =cur.fetchall()
    #game_name = "ranking_mahojin"
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f'SELECT * FROM {game_name}')
    results =cur.fetchall()
    dict_result =[]
    for row in results:
        dict_result.append(dict(row))
    cur.close()
    conn.close()
    return dict_result

