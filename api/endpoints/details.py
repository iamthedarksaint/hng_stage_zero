# api/endpoints/details.py
from fastapi import APIRouter
from sqlalchemy import create_engine
import pandas as pd
from decouple import config

router = APIRouter()

# Function to fetch data from the 'details' table
def get_data_from_db():
    user = config("USER")
    host = config("HOST")
    port = config("PORT")
    password = config("PASSWORD")
    database = config("DATABASE")

    db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(db_url, pool_size=1, max_overflow=1)

    # Retrieve the data as a DataFrame
    df = pd.read_sql("SELECT * FROM details", con=engine)
    return df

# Route to retrieve data
@router.get("/details/")
def get_details():
    df = get_data_from_db()
    # Convert the DataFrame to JSON format
    return df.to_dict(orient="records")
