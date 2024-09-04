import json
import sqlite3


class Database:
    def __init__(self, db_file="search_engine.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS pages (
            url TEXT PRIMARY KEY,
            title TEXT,
            content TEXT,
            snippet TEXT,
            last_crawled TEXT
        )
        """
        )

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS links (
            from_url TEXT,
            to_url TEXT,
            PRIMARY KEY (from_url, to_url)
        )
        """
        )

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS index_data (
            word TEXT,
            url TEXT,
            tf REAL,
            PRIMARY KEY (word, url)
        )
        """
        )

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS idf_data (
            word TEXT PRIMARY KEY,
            idf REAL
        )
        """
        )

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS pagerank (
            url TEXT PRIMARY KEY,
            score REAL
        )
        """
        )

        self.conn.commit()

    def save_page(self, url, title, content, snippet, last_crawled):
        self.cursor.execute(
            """
        INSERT OR REPLACE INTO pages (url, title, content, snippet, last_crawled)
        VALUES (?, ?, ?, ?, ?)
        """,
            (url, title, content, snippet, last_crawled),
        )
        self.conn.commit()

    def save_links(self, links):
        self.cursor.executemany(
            """
        INSERT OR REPLACE INTO links (from_url, to_url) VALUES (?, ?)
        """,
            [
                (from_url, to_url)
                for from_url, to_urls in links.items()
                for to_url in to_urls
            ],
        )
        self.conn.commit()

    def save_index_data(self, index):
        self.cursor.executemany(
            """
        INSERT OR REPLACE INTO index_data (word, url, tf) VALUES (?, ?, ?)
        """,
            [
                (word, url, tf)
                for word, urls in index.items()
                for url, tf in urls.items()
            ],
        )
        self.conn.commit()

    def save_idf_data(self, idf):
        self.cursor.executemany(
            """
        INSERT OR REPLACE INTO idf_data (word, idf) VALUES (?, ?)
        """,
            idf.items(),
        )
        self.conn.commit()

    def save_pagerank(self, pagerank):
        self.cursor.executemany(
            """
        INSERT OR REPLACE INTO pagerank (url, score) VALUES (?, ?)
        """,
            pagerank.items(),
        )
        self.conn.commit()

    def load_pages(self):
        self.cursor.execute("SELECT * FROM pages")
        return {
            row[0]: {
                "title": row[1],
                "content": row[2],
                "snippet": row[3],
                "last_crawled": row[4],
            }
            for row in self.cursor.fetchall()
        }

    def load_links(self):
        self.cursor.execute("SELECT * FROM links")
        links = {}
        for row in self.cursor.fetchall():
            if row[0] not in links:
                links[row[0]] = []
            links[row[0]].append(row[1])
        return links

    def load_index_data(self):
        self.cursor.execute("SELECT * FROM index_data")
        index = {}
        for row in self.cursor.fetchall():
            if row[0] not in index:
                index[row[0]] = {}
            index[row[0]][row[1]] = row[2]
        return index

    def load_idf_data(self):
        self.cursor.execute("SELECT * FROM idf_data")
        return dict(self.cursor.fetchall())

    def load_pagerank(self):
        self.cursor.execute("SELECT * FROM pagerank")
        return dict(self.cursor.fetchall())

    def close(self):
        self.conn.close()
