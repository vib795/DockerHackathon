from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime as SQLAlchemyDateTime
from datetime import datetime
import logging
from dotenv import load_dotenv
import os
from datetime import timedelta

# Load environment variables
load_dotenv()

Base = declarative_base()

# Define the Reminder model
class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    date = Column(String, nullable=True)
    time = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    trigger_time = Column(DateTime, nullable=True)  # New field for trigger time

def create_session():
    try:
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME')
        container_name = os.getenv('CONTAINER_NAME')

        logging.info(f"'postgresql://' + {db_user} + ':' + {db_password} + '@' + {container_name} + '/' + {db_name}")

        # Replace 'your_db_container_name' with the actual name of your PostgreSQL container
        db_url = 'postgresql://' + db_user + ':' + db_password + '@' + container_name + '/' + db_name

        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)
    except Exception as e:
        logging.error(f"Error occurred in creating DB session. - {str(e)}")
        raise Exception(f"Error occurred in creating DB session. - {str(e)}")

# Function to trigger alerts for reminders
def trigger_alert(reminder):
    # Implement code to trigger an alert at the specified time for the reminder
    print(f"Alert for Reminder: {reminder.text}")

# Function to check for due reminders and trigger alerts
def check_and_trigger_alerts():
    Session = create_session()  # Create a session class, not an instance
    session = Session()  # Create a session instance
    current_time = datetime.now()
    due_reminders = session.query(Reminder).filter(Reminder.trigger_time <= current_time).all()
    session.close()
    for reminder in due_reminders:
        trigger_alert(reminder)
        # You may want to mark the reminder as "notified" to avoid re-triggering it.



# Example of inserting a reminder with a trigger time
def insert_reminder(text, date, time, trigger_time):
    try:
        # Parse the date and time strings into datetime objects
        reminder_date = datetime.strptime(date, '%Y-%m-%d')
        reminder_time = datetime.strptime(time, '%H:%M')
        trigger_time = datetime(reminder_date.year, reminder_date.month, reminder_date.day, reminder_time.hour, reminder_time.minute) - timedelta(hours=1)
        Session = create_session()  # Create a session class, not an instance
        session = Session()  # Create a session instance
        reminder = Reminder(text=text, date=date, time=time, timestamp=datetime.utcnow(), trigger_time=trigger_time)
        session.add(reminder)
        session.commit()
        session.close()
    except Exception as e:
        logging.error(f"Error occurred in inserting values to REMINDERS table. - {str(e)}")
        raise Exception(f"Error occurred in inserting values to REMINDERS table. - {str(e)}")

def get_reminders():
    try:
        reminders_list = []
        Session = create_session()  # Create a session class, not an instance
        session = Session()  # Create a session instance
        reminders = session.query(Reminder).all()
        session.close()
        for reminder in reminders:
            reminders_list.append(f"Message: {reminder.text}, Date: {reminder.date}, Time: {reminder.time}")
        return reminders_list
    except Exception as e:
        logging.error(f"Error occurred in fetching REMINDERS from DB. - {str(e)}")
        raise Exception(f"Error occurred in fetching REMINDERS from DB. - {str(e)}")




# Example usage:

# Insert a reminder
# insert_reminder("Buy groceries", datetime(2023, 10, 17), datetime(2023, 10, 17, 15, 30))

# # Retrieve reminders
# reminders = get_reminders()
# for reminder in reminders:
#     print(f"Reminder: {reminder.text}, Date: {reminder.date}, Time: {reminder.time}")
