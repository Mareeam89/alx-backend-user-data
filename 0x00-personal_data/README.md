## Project Description
Learn examples of Personally Identifiable Information (PII).
How to implement a log filter that will obfuscate PII fields.
How to encrypt a password and check the validity of an input password.
How to authenticate to a database using environment variables.


* **0. Regex-ing** - Write a function called `filter_datum` that returns the log message obfuscated. - `filtered_logger.py`.
* **1. Log formatter** - Copy the following code into filtered_logger.py and do the given steps. - `filtered_logger.py`.
* **2. Create logger** - Implement a `get_logger` function that takes no arguments and returns a `logging.Logger` object. - `filtered_logger.py`.
* **3. Connect to secure database** - Implement a `get_db` function that returns a connector to the database (`mysql.connector.connection.MySQLConnection object`). - `filtered_logger.py`.
* **4. Read and filter data** - Implement a `main` function that takes no arguments and returns nothing. - `filtered_logger.py`.
* **5. Encrypting passwords** - Implement a `hash_password` function that expects one string argument name `password` and returns a salted, hashed password, which is a byte string. - `encrypt_password.py`.
arguments and returns nothing. - `filtered_logger.py`.
* **6. Check valid password** - Implement an `is_valid` function that expects 2 arguments and returns a boolean. - `encrypt_password.py`.

