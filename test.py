from search_engine_func.page_rank import pagerank
from search_engine_func.crawler import crawler_bot
from database_helper import get_all_page_outlinks, get_all_inverted_indexes

if __name__ == "__main__":

    crawler_bot("https://en.wikipedia.org/wiki/Google")

    # graph={}

    # for page in get_all_page_outlinks():
    #     graph[page["url"]] = page.get("outlinks", [])
    
    # print(pagerank(graph))

    
    