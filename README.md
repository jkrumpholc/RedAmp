# RedAmp Python Developer Assignment

### 1. Preparing the environment

- Dependencies:
  - Python 3.11
  - To install Python dependencies, run: `pip install -r requirements.txt`
  - Used libraries:
    - psycopg2
    - requests
    - dotenv


- Credentials file
  - Credentials `.env` file is attached to e-mail
  - File contains login credentials to database 
  - Script won't work without attached (or custom) `.env` file
  - File should be copied into root folder of project


- Database:
  - Database is already created on remote server, credentials are in attachment of response mail.
  - Database schema is saved in file [create_tables.sql](scripts%2Fcreate_tables.sql)`
  - To clean up database, you can run [clear_database.sql](scripts%2Fclear_database.sql)
  - If you want to use different database, edit `.env` file with new items: `DATABASE_HOST`, `DATABASE_NAME`, `DATABASE_USERNAME` and `DATABASE_PASSWORD`

### 2. Starting script

- Syntax: `python3 main.py --file [name_of_file_with_links]`
- Parameter `--file` should be path to file with links.
- Script also have parameter `--help`, which will show basic help.
- If started without arguments, script will return error message: 
`No input data`
`Please set argument '--file'. For info use '--help'`
 

### 3. Testing

- Project contains few unit/integration tests for whole scope of project.
- Tests are stored in [tests.py](test%2Ftests.py)
- Tests can be run by: `python3 tests.py`
