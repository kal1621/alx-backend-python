import sqlite3  # or your database module

def stream_user_ages():
    """Generator to yield user ages one by one from the database."""
    connection = sqlite3.connect('path_to_your_database.db')  # Update with your database path
    cursor = connection.cursor()

    cursor.execute("SELECT age FROM user_data")  # Assuming 'age' is the column name
    for row in cursor:
        yield row[0]  # Yield the age (assuming it's in the first column)

    cursor.close()
    connection.close()

def calculate_average_age():
    """Calculate the average age of users using the age generator."""
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        return 0  # Prevent division by zero

    average_age = total_age / count
    return average_age

if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")  # Print average age formatted to 2 decimal places
