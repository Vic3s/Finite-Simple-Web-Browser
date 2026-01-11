from search_engine_func.page_rank import page_rank
from search_engine_func.crawler import crawler_bot
from database_helper import get_all_page_outlinks, get_all_inverted_indexes
from search_engine_func.search_by_words import search, get_wordlist

if __name__ == "__main__":

    # crawler_bot("https://en.wikipedia.org/wiki/Google")

    search(get_wordlist(["search", "with", "google"]))
    
    