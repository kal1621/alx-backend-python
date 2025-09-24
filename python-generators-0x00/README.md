# Python Database Connection and Data Insertion

This project demonstrates how to connect to a database, create a table, and insert data using Python. It utilizes a custom module `seed` for database operations.

## Requirements

- Python 3.x
- Required Python packages (if any, specify here)

## Files

- `0-main.py`: The main script that connects to the database, creates a table, and inserts data.
- `seed.py`: A module that contains functions for database connection and operations.
- `user_data.csv`: A CSV file containing user data to be inserted into the database.

## Functionality

1. **Database Connection**: 
   - Connects to a database using the `connect_db` function from the `seed` module.
   - Creates a database named `ALX_prodev`.

2. **Table Creation**:
   - Creates a table named `user_data` in the `ALX_prodev` database.

3. **Data Insertion**:
   - Inserts data from `user_data.csv` into the `user_data` table.

4. **Data Retrieval**:
   - Retrieves the first five rows from the `user_data` table and prints them.

## Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python-generators-0x00
