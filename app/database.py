import os
from motor.motor_asyncio import AsyncIOMotorClient

_client = None

async def connect_db():
    global _client
    _client = AsyncIOMotorClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017'))
    print('MongoDB connected')

async def disconnect_db():
    if _client:
        _client.close()

def get_db():
    db_name = os.getenv('DB_NAME', 'appdb')
    return _client[db_name]
