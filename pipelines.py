import sqlite3

class MoviePipeline:

    def __init__(self):
        self.con = sqlite3.connect('movies.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS theaters(theater TEXT, movie TEXT)")   

    def process_item(self, item, spider):
        try:
            self.cur.execute('INSERT INTO theaters(theater, movies) VALUES (?, ?)',
                            (
                                item['theater'],
                                item['movies']
                            ))

            self.con.commit()
        except Exception:
            spider.logger.error(f'Error inserting item into database')
        return item
    
    def close_spider(self, spider):
        self.con.close()