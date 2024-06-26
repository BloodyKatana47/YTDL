import sqlite3
from typing import List, Tuple

from config import settings

ADMIN_ID: int = settings.admin_id


class Database:
    def __init__(self, db_file: str) -> None:
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        """
        Creates tables if they do not exist.
        """

        with self.connection:
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE NOT NULL,
                    first_name VARCHAR(64) NOT NULL,
                    username VARCHAR(32) UNIQUE,
                    status BOOL NOT NULL,
                    is_superuser BOOL NOT NULL,
                    is_active BOOL,
                    number_of_downloads INTEGER DEFAULT (0)
                );
                '''
            )
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS links(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_id VARCHAR NOT NULL,
                    url VARCHAR(11) NOT NULL
                );
                '''
            )
            self.cursor.execute(
                '''
                INSERT OR IGNORE INTO users (
                    user_id,
                    first_name,
                    status,
                    is_superuser,
                    is_active
                )
                VALUES (?, ?, ?, ?, ?);
                ''', (ADMIN_ID, 'admin', 0, 1, 1)
            )

    def user_exists(self, user_id: int) -> bool:
        """
        Checks if a user exists in the database.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                SELECT user_id
                FROM users
                WHERE user_id = ?;
                ''', (user_id,)
            ).fetchone()
            return False if result is None else True

    def create_user(self, user_id: int, first_name: str, username: str) -> sqlite3.Cursor:
        """
        Creates a new user.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                INSERT INTO users (
                    user_id,
                    first_name,
                    username,
                    status,
                    is_superuser,
                    is_active
                )
                VALUES (?, ?, ?, ?, ?, ?);
                ''', (user_id, first_name, username, 0, 0, 1)
            )
            return result

    def set_active(self, user_id: int, is_active: int) -> sqlite3.Cursor:
        """
        Sets user as active.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                UPDATE users
                SET is_active = ?
                WHERE user_id = ?;
                ''', (is_active, user_id)
            )
            return result

    def get_users(self) -> List[Tuple[int, int]]:
        """
        Lists all users.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                SELECT user_id,
                    is_active
                FROM users;
                '''
            ).fetchall()
            return result

    def is_admin(self, user_id: int) -> Tuple[int]:
        """
        Checks if user is an admin.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                SELECT is_superuser
                FROM users
                WHERE user_id = ?;
                ''', (user_id,)
            ).fetchone()
            return result

    def set_status(self, user_id: int, status: int) -> sqlite3.Cursor:
        """
        Changes user's downloading status.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                UPDATE users
                SET status = ?
                WHERE user_id = ?;
                ''', (status, user_id)
            )
            return result

    def see_status(self, user_id: int) -> Tuple[int]:
        """
        Shows user's downloading status.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                SELECT status
                FROM users
                WHERE user_id = ?;
                ''', (user_id,)
            ).fetchone()
            return result

    def increase_nod(self, user_id: int) -> sqlite3.Cursor:
        """
        Increases user's number of downloads.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                UPDATE users
                SET number_of_downloads = number_of_downloads + 1
                WHERE user_id = ?;
                ''', (user_id,)
            )
            return result

    def file_exists(self, url: str) -> Tuple[str]:
        """
        Checks if file_id with given url exists and returns file_id if one exists.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                SELECT file_id
                FROM links
                WHERE url = ?;
                ''', (url,)
            ).fetchone()
            return result

    def file_save(self, file_id: str, url: str) -> sqlite3.Cursor:
        """
        Saves file_id with given url.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                INSERT INTO links (
                    file_id,
                    url
                )
                VALUES (?, ?);
                ''', (file_id, url)
            )
            return result

    def update_user(self, user_id: int, first_name: str, username: str, is_active: int) -> sqlite3.Cursor:
        """
        Updates data about user.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                UPDATE users
                SET first_name = ?,
                    username = ?,
                    is_active = ?
                WHERE user_id = ?;
                ''', (first_name, username, is_active, user_id)
            )
            return result
