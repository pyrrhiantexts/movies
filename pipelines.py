import sqlite3

class MoviePipeline:

    def __init__(self):
        self.con = sqlite3.connect('movies.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE theaters(theater, movie)")   

    def process_item(self, item, spider):
        self.cur.execute('INSERT INTO theaters(theater, movies) VALUES (?, ?)',
                         (
                             item('theater'),
                             item('movies')
                         ))

            self.con.commit()
        return item