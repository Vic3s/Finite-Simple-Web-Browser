import re
from database_helper import insert_singel_page, get_all_inverted_indexes, bulk_write_inverted_indexes
from pymongo import UpdateOne, InsertOne

def index(webpage, webpage_url):
    # get the title of the page
    title_tag = webpage.find("title")
    title = title_tag.get_text(strip=True) if title_tag else "Missing Title"

    # get the desctiption
    description = ""
    meta_desctipntion = webpage.find("meta", attrs={"name": "description"})
    if meta_desctipntion and "content" in meta_desctipntion.attrs:
        description = meta_desctipntion["content"]
    else:
        text_content = webpage.get_text(separator=" ", strip=True)
        description = text_content[:200] + "..." if len(text_content) > 200 else text_content

    # get the word content of the page
    words = re.findall(r"\b\w+\b", webpage.get_text(separator=" ", strip=True).lower())

    # double check and filter out any numbers and charachters and remove duplicate 
    words = [word for word in words if word.isalpha()]
    unique_words = set(words)

    # save inverted indexes for page content
    all_existing_words_list = get_all_inverted_indexes().keys()
    operations = []

    for word in unique_words:
        if word in all_existing_words_list:
            operations.append(
                UpdateOne(
                    {"word": word},
                    {"$addToSet": {"word_pages": webpage_url}}
                )
            )
            
        else:
            operations.append(
                InsertOne({
                    "word": word,
                    "word_pages": [webpage_url]
                })
            )
    
    bulk_write_inverted_indexes(operations)
    
    # save page content 
    indexed_page = {
        "url": webpage_url,
        "title": title,
        "description": description,
        "words": words
    }

    try:
        insert_singel_page(indexed_page)
    except Exception as ex:
        print(f"Couldnt save indexed page: {ex}")
    
    print("page saved")

