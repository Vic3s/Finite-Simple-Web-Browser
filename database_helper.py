import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

cluster = MongoClient(os.getenv("DB_STRING"))

db = cluster["search_index"]
collection = db["page_info"]

def insert_singel_item(page: dict):
    collection.insert_one(page)

def get_all_items():
    all_pages = collection.find()
    all_pages_list = [page for page in all_pages]

    return all_pages_list
