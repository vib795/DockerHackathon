from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging
from dotenv import load_dotenv
import os


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
    trigger_time = Column(DateTime, nullable=False)  # New field for trigger time


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
    print(f"Alert for Reminder: {reminder.text} \n")

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

