import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT user_id from users WHERE user_id = ?', (user_id,)).fetchone()
            return False if result is None else True

    def create_user(self, user_id, first_name, username):
        with self.connection:
            result = self.cursor.execute(
                'INSERT INTO users (user_id, first_name, username, status, is_superuser, is_active) VALUES (?, ?, ?, ?, ?, ?)',
                (user_id, first_name, username, 0, 0, 1,))
            return result

    def set_active(self, user_id, is_active):
        with self.connection:
            result = self.cursor.execute('UPDATE users SET is_active = ? WHERE user_id = ?', (is_active, user_id,))
            return result

    def get_users(self):
        with self.connection:
            result = self.cursor.execute('SELECT user_id, is_active FROM users').fetchall()
            return result

    def is_admin(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT is_superuser FROM users WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def set_status(self, user_id, status):
        with self.connection:
            result = self.cursor.execute('UPDATE users SET status = ? WHERE user_id = ?', (status, user_id,))
            return result

    def see_status(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT status FROM users WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def increase_nod(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                '''UPDATE users SET number_of_downloads = number_of_downloads + 1 WHERE user_id = ?;''',
                (user_id,))
            return result

    def file_exists(self, url):
        with self.connection:
            result = self.cursor.execute('SELECT file_id FROM links WHERE url = ?', (url,)).fetchone()
            return result

    def file_save(self, file_id, url):
        with self.connection:
            result = self.cursor.execute('INSERT INTO links (file_id, url) VALUES (?, ?)', (file_id, url,))
            return result
