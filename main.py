# main.py
from fastapi import FastAPI
from api.endpoints.details import router as details_router
from app.services.details_service import create_data, upload_to_database

app = FastAPI()

# Upload data to the database on app startup
@app.on_event("startup")
async def startup_event():
    # Step 1: Create the DataFrame
    df = create_data()

    # Step 2: Upload the DataFrame to the database
    upload_to_database(df)

app.include_router(details_router)
