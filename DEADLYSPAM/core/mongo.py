import os
import config
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient




_mongo_async_ = _mongo_client_(config.DB_URI)
_mongo_sync_ = MongoClient(config.DB_URI)
mongodb = _mongo_async_.Deadly
pymongodb = _mongo_sync_.Deadly
