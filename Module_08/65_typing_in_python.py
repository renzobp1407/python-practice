# Python is a Dinamically typed languajes, a object can have any other type of value depending on the declaration

tell to the editor what your functions return and what your parameters types will recieve


def create_book_table() -> None: # this is typing with the none
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
        cursor.execute('CREATE TABLE books (id integer primary key, name text, author text, read integer default 0)')


def get_all_books() -> List[Book]: # Recieve a list
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    return books


def __enter__(self) -> sqlite3.Connection:  # another example with a exclusive variable
    self.connection = sqlite3.connect(self.host)
    return self.connection