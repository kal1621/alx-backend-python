import sqlite3
import functools

#### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(query, *args, **kwargs):
        # Log the SQL query (query is guaranteed to be first positional argument)
        print(f"Executing SQL query: {query}")
        
        # Call the original function
        return func(query, *args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users("SELECT * FROM users")  # Remove query= keyword
