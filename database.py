import os
import sqlite3
import uuid
from datetime import datetime

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, CHAR, DateTime, text

conn = sqlite3.connect('db/app.db')
cursor = conn.cursor()

db_path = os.path.join("db", "app.db")
engine = db.create_engine(f"sqlite:///{db_path}", echo=True)
connection = engine.connect()
metadata = db.MetaData()

Base = db.declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)

    uploads = db.relationship('Upload', back_populates='user', cascade='all, delete-orphan')


class Upload(Base):
    __tablename__ = 'uploads'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    filename = Column(String, nullable=False)
    upload_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    finish_time = Column(DateTime)
    status = Column(String, nullable=False)

    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='uploads')
    # Additional upload statuses for better tracking
    STATUS_PENDING = "pending"
    STATUS_PROCESSING = "processing"
    STATUS_DONE = "done"
    STATUS_FAILED = "failed"

    # Constraints for the status column
    VALID_STATUSES = {STATUS_PENDING, STATUS_PROCESSING, STATUS_DONE, STATUS_FAILED}

    # Add an upload_path method to compute the path of the uploaded file
    def upload_path(self) -> str:
        # Assuming the uploaded files are stored in an 'uploads' folder
        return os.path.join("uploads", self.uid)

    # Add a method to set finish_time under the right circumstances
    def set_finish_time(self, finish_time: datetime.datetime, status: str):
        # Only set finish_time if the status is 'done' or 'failed'
        if status in {Upload.STATUS_DONE, Upload.STATUS_FAILED}:
            self.finish_time = finish_time
        else:
            raise ValueError("Invalid status for setting finish_time")

    # Add a method to see error messages for failed uploads
    def get_error_message(self) -> str:
        # Assuming error messages are stored in a 'logs' folder with the same filename as the upload
        log_file_path = os.path.join("logs", f"{self.uid}.log")
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as log_file:
                return log_file.read()
        else:
            return "No error message found for this upload"

    # Override __repr__ for a better representation of the Upload object
    def __repr__(self):
        return f"<Upload(id={self.id}, uid={self.uid}, filename='{self.filename}', status='{self.status}')>"


# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = db.sessionmaker(bind=engine)
session = Session()

# Create a new user and upload for testing
user1 = User(email='user1@example.com')
upload1 = Upload(filename='file1.txt', status=Upload.STATUS_PENDING)
user1.uploads.append(upload1)

# Add the user and upload to the session and commit the changes
session.add(user1)
session.commit()

# Query the database to verify the data is stored correctly
users = session.query(User).all()
uploads = session.query(Upload).all()

print("Users:")
for user in users:
    print(f"User ID: {user.id}, Email: {user.email}")

print("\nUploads:")
for upload in uploads:
    print(f"Upload ID: {upload.id}, User ID: {upload.user_id}, Filename: {upload.filename}, Status: {upload.status}")

# Close the session when done
session.close()
