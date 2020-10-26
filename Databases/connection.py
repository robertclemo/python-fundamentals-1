import psycopg2
import os
from os import getenv
from os import environ

# **** WINDOWS ******
# Download Anaconda and then install psycopg2


# First install python-dotenv
# import os
# from dotenv import load_dotenv
# call method load_dotenv()

# conn = psycopg2.connect(
#     database = getenv('DB_NAME'),  
#     user =  getenv('DB_USER'), 
#     password = getenv('DB_PASSWORD'), 
#     host = getenv('DB_URL'), 
#     port = getenv('DB_PORT'), 
# )

# create .env file under the root directory/folder and add the following lines:
# export DB_NAME="database_name"
# export DB_USER="database_user"
# export DB_URL="database_host"
# export DB_PASSWORD="database_password"
# export DB_PORT="database_port"
# ***** END OF WINDOWS *********

# ** ANOTHER WAY TO INSTALL python-dotenv
# conda install -c conda-forge python-dotenv

# *********** MacOS ****************
conn = psycopg2.connect(
    database = environ.get('DB_NAME'),  
    user = environ.get('DB_USER'), 
    password = environ.get('DB_PASSWORD'), 
    host = environ.get('DB_URL'), 
    port = environ.get('DB_PORT'), 
)
# ******** END OF MacOS ********



def retrieveUser():
    try: 
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        if(rows):
            for row in rows:
                print(f'''
                Id:..............{row[0]}
                username:........{row[1]}
                password:........{row[2]} 
                ''')
            cursor.close()
        else:
            print('Your database has no data')

        # SQL => Structured Query Language => Language for SQL Databases
        # C => Create => INSERT
        # R => Read => SELECT 
        # U => Update => UPDATE
        # D => Delete => DELETE
    except(Exception, psycopg2.Error) as error:
        print('Error while fetching data from PostgreSQL', error)


retrieveUser()