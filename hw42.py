import psycopg2

def load_data_to_database(file_path, db_connection):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip()
            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO table_name (column_name) VALUES (%s)", (data,))
            db_connection.commit()
            cursor.close()

def export_data_to_file(file_path, db_connection):
    with open(file_path, 'w') as file:
        cursor = db_connection.cursor()
        cursor.execute("SELECT column_name FROM table_name")
        for row in cursor:
            data = row[0]  
            file.write(data + '\n')
        cursor.close()

db_connection = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_user",
    password="your_password"
)

load_data_to_database("input.txt", db_connection)

export_data_to_file("output.txt", db_connection)

db_connection.close()
