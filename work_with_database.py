import sqlite3


def insert_information_to_database(sender_id, nickname):
    db = sqlite3.connect('nicknames.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS nicknames (
        user_id INT,
        nickname TEXT
    )""")

    db.commit()
    sql.execute("SELECT user_id FROM nicknames")
    nicknames = sql.fetchall()
    if (sender_id,) not in nicknames:
        sql.execute("INSERT INTO nicknames VALUES(?, ?)", (sender_id, nickname))
    else:
        sql.execute(f"UPDATE nicknames SET nickname = '{nickname}' WHERE user_id = {sender_id}")


    db.commit()



