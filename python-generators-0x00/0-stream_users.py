import sqlite3  # or your database module

def stream_users():
    # Establish a database connection
    connection = sqlite3.connect('path_to_your_database.db')  # Update with your database path
    cursor = connection.cursor()

    # Execute the SQL query to fetch all rows from the user_data table
    cursor.execute("SELECT * FROM user_data")

    # Use a for loop to iterate over the cursor and yield each row
    for row in cursor:
        yield row

    # Close the cursor and connection after use
    cursor.close()
    connection.close()

# Example usage
if __name__ == "__main__":
    for user in stream_users():
        print(user)
