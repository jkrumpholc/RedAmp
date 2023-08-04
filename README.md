# RedAmp Python Developer Assignment

### 0. Preparing the environment

- Dependencies:
  - Python 3.11
  - To install Python dependencies, run: `pip install -r requirements.txt`
  - Used libraries:
    - psycopg2
    - requests
    - dotenv


- Database:
  - Database is already created on remote server, credentials are in attachment of response mail.
  - Database schema is saved in file [create_tables.sql](scripts%2Fcreate_tables.sql)`
  - To clean up database, you can run [clear_database.sql](scripts%2Fclear_database.sql)
  - If you want to use different database, edit `.env` file with new items: `DATABASE_HOST`, `DATABASE_NAME`, `DATABASE_USERNAME` and `DATABASE_PASSWORD`

### 1. Starting script

- Syntax: `python3 main.py --file [name_of_file_with_links]`
- If started without argument file, script will return error message: 
`No input data`
`Please set argument '--file'. For info use '--help'`
- Script also have parameter `--help`, which will show basic help. 


