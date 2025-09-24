import sqlite3  # or your database module

def stream_users_in_batches(batch_size):
    """Generator to fetch rows in batches from the user_data table."""
    connection = sqlite3.connect('path_to_your_database.db')  # Update with your database path
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data")
    
    while True:
        batch = cursor.fetchmany(batch_size)  # Fetch a batch of rows
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Process each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user[2] > 25]  # Assuming age is in the 3rd column (index 2)
        yield filtered_users  # Yield the filtered results

# Example usage
if __name__ == "__main__":
    for processed_batch in batch_processing(10):  # Set the desired batch size
        for user in processed_batch:
            print(user)
