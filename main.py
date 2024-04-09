# main.py

from fastapi import FastAPI
from dotenv import load_dotenv
from config.settings import get_settings
from db.connection import connection
from api.routers import studentrouter
load_dotenv()
app = FastAPI()






print(get_settings().mongodb_uri)
print("comming up here at main again aftering hitting middleware")
app.include_router(studentrouter)

@app.get("/info")
async def get_info():
    return {"message": "Student API is running"}



