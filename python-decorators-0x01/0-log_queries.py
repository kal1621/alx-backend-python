import sqlite3
import functools

#### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query from arguments (assuming it's a keyword argument named 'query')
        query = kwargs.get('query', '') if kwargs else ''
        
        # If query is not in kwargs, check if it's in args (assuming it's the first positional argument)
        if not query and args and len(args) > 1:
            query = args[1] if isinstance(args[1], str) else ''
        
        # Log the SQL query
        print(f"Executing SQL query: {query}")
        
        # Call the original function
        return func(*args, **kwargs)
    
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
users = fetch_all_users(query="SELECT * FROM users")
