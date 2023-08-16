SQL Introduction Project

This project is designed to provide an introduction to SQL (Structured Query Language) using MySQL 8.0 on Ubuntu 20.04 LTS. It covers various SQL queries and concepts to help you get started with database manipulation and querying.
Project Files

The project consists of the following files:

    my_script.sql: This file contains SQL queries that demonstrate various concepts. Each query is preceded by a comment explaining its purpose.

    README.md: This file (the current document) provides an overview of the project, its contents, and instructions for setup and usage.

Setup

Follow these steps to set up the MySQL 8.0 environment on Ubuntu 20.04 LTS:

    Update the package list:

    bash

$ sudo apt update

Install MySQL Server:

bash

$ sudo apt install mysql-server

Verify the installation:

bash

$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

Connect to the MySQL server:

bash

    $ sudo mysql
    Welcome to the MySQL monitor. Commands end with ; or \g.
    Your MySQL connection id is 11
    Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql>

SQL Queries

The my_script.sql file contains a set of SQL queries showcasing various concepts. Each query is accompanied by a comment explaining its syntax and purpose. For example:

sql

-- Retrieve the 3 most recent students from Batch ID=3
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

Feel free to explore the my_script.sql file to learn more about different SQL queries.
Project Usage

To execute the SQL queries in the my_script.sql file, follow these steps:

    Open the MySQL command-line interface:

    bash

$ sudo mysql

Choose a database if needed:

sql

USE your_database_name;

Execute the SQL queries from my_script.sql using the source command:

sql

    source path/to/my_script.sql;

Conclusion

This project serves as an introductory guide to SQL using MySQL 8.0 on Ubuntu 20.04 LTS. By following the provided instructions, you can set up the environment, explore SQL queries, and enhance your understanding of database manipulation. Enjoy learning and experimenting with SQL!