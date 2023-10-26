import psycopg2
import os

# Connection parameters
db_host = "db"  # This should match the service name in your docker-compose.yml
db_name = "docker_hackathon_db"
db_user = "singh"
db_password = os.environ['DB_PASSWORD']

# Connect to the database
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

# Perform database operations
cursor = conn.cursor()
cursor.execute("INSERT INTO reminders (text, date, time) VALUES (%s, %s, %s)", (reminder_text, reminder_date, reminder_time))
conn.commit()

# Close the connection
conn.close()
