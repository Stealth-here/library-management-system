from dp import get_connection

def add_book(title, author, year, isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                   (title, author ,year, isbn))
    conn.commit()
    conn.close()

def view_book():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_book(title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title=?", ('%' + title + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_book(book_id, title, author, year, isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author,year,isbn,book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

