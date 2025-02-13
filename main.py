from fastapi import FastAPI
from routes import router as api_router
from utils.mongodb import db

app = FastAPI()


async def connection():
    try:
        # await db.client.admin.command("ismaster")
        await db.command("ping")
        print("==>   Connected to MongoDB")
    except Exception as e:
        print(e)
        raise e


app.add_event_handler("startup", connection)
app.include_router(api_router, prefix="/api")
