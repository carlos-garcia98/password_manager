To use the password manager:
    1) install the require modules.
    2) Create a Database with PostgreSQL.
    3) Create a Table within the Database with the following columns:
        id_accont [serial, not null, primary key]
        app_name [character varying, not null]
        username [character varying, not null]
        password [character varying, not null]
        url [character varying, not null]
    4) You have to change the database information that is in the connection.py file wiht you database information.
    5) In the app_menu.py file is a variable named hashed_password, change the content of that variable with your own hashed password (use the hash_passwords.py file to get a hashed password).