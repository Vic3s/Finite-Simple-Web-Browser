import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from search_engine_func.additional_functionality import chunk

load_dotenv()

cluster = MongoClient(os.getenv("DB_STRING"))

db = cluster["search_index"]
collection_page = db["page_info"]
collection_outlinks = db["page_outlinks"]
collection_inverted_indexes = db["inverted_indexes"]

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

def get_all_inverted_indexes():
    all_inverted_indexes = collection_inverted_indexes.find()
    return {inverted_index_obj["word"]: inverted_index_obj["word_pages"] for inverted_index_obj in all_inverted_indexes}

# def insert_single_inverted_index(inverted_index: dict):
#     collection_inverted_indexes.insert_one(inverted_index)

# def update_inverted_index(word: str, page: str):
#     filter_query = {"word": word.lower()}
#     update_values = {"$addToSet": { "word_pages": page.lower()}}

#     collection_inverted_indexes.update_one(filter_query, update_values)

def bulk_write_inverted_indexes(operations: list):
    if operations:
        for batch in chunk(operations, 500):
            collection_inverted_indexes.bulk_write(batch)

