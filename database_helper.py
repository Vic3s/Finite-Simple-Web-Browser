import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

cluster = MongoClient(os.getenv("DB_STRING"))

db = cluster["search_index"]
collection_page = db["page_info"]
collection_outlinks = db["page_outlinks"]

def insert_singel_page(page: dict):
    collection_page.insert_one(page)

def get_all_pages():
    all_pages = collection_page.find()
    all_pages_list = [page for page in all_pages]

    return all_pages_list

def insert_singel_page_outlinks(page_outlinks_obj: dict):
    collection_outlinks.insert_one(page_outlinks_obj)

def get_all_page_outlinks():
    all_page_outlinks = collection_outlinks.find()
    all_page_outlinks_list = [page_outlinks_obj for page_outlinks_obj in all_page_outlinks]

    return all_page_outlinks_list
