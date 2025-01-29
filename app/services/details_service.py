# app/services/details_service.py
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from decouple import config

# Function to create DataFrame
def create_data():
    current_datetime = datetime.now()

    data = {
        "email": "bojzino128@gmail.com",
        "current_datetime": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "github_url": "https://github.com/iamthedarksaint"
    }
    df = pd.DataFrame([data])
    df['current_datetime'] = pd.to_datetime(df["current_datetime"], errors='coerce')
    return df

# Function to upload the DataFrame to the database
def upload_to_database(df: pd.DataFrame):
    user = config("USER")
    host = config("HOST")
    port = config("PORT")
    password = config("PASSWORD")
    database = config("DATABASE")

    db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(db_url, pool_size=1, max_overflow=1)

    # Upload the DataFrame to the 'details' table
    df.to_sql("details", con=engine, if_exists="replace", index=False)
    print("Data successfully loaded to the database")
