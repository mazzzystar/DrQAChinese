import sqlite3


save_path = "/Users/ke/Documents/DATASET/DrQA/cnWikiDB/cnwiki.db"


def get_title(id):
    conn = sqlite3.connect(save_path)
    c = conn.cursor()
    c.execute("SELECT id, title from documents WHERE id=?;", (id, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows


# print(get_title(str(5561198)))