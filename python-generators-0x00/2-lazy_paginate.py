import sqlite3  # or your database module

def paginate_users(page_size, offset):
    """Fetch a page of users from the database."""
    connection = sqlite3.connect('path_to_your_database.db')  # Update with your database path
    cursor = connection.cursor()

    query = "SELECT * FROM user_data LIMIT ? OFFSET ?"
    cursor.execute(query, (page_size, offset))
    
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return users

def lazy_paginate(page_size):
    """Generator to lazily load each page of users."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)  # Fetch the next page
        if not page:
            break
        yield page
        offset += page_size  # Increment the offset for the next page

# Example usage
if __name__ == "__main__":
    for page in lazy_paginate(10):  # Set the desired page size
        for user in page:
            print(user)
