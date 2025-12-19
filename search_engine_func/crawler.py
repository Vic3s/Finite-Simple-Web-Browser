from bs4 import BeautifulSoup
import requests
import time
import random
from . import indexer
from . import page_graph

def crawler_bot(starter_url: str):
    urls = [starter_url]
    visited_urls = set()
    outlinks_formated=[]

    headers = {
        "User-Agent": "MySimpleCrawler/1.0 (learning project)"
    }

    # go through all urls while there are any in the list
    while urls:
        # gets the next url
        current_url = urls.pop()
        print("crawling: " + current_url)
        time.sleep(random.uniform(1, 3))
        try:
            response = requests.get(current_url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Faild do retrieve {current_url}: {e}")
            continue

        # get the content of the page
        webpage = BeautifulSoup(response.content, "html.parser")

        # give the page content to the indexer 
        indexer.indexer(webpage, current_url)

        # get the hyperlinks from the html text
        hyperlinks = webpage.select("a[href]")

        for hyperlink in hyperlinks:
            url = hyperlink["href"]

            # formating the url properly
            if url.startswith("#"):
                continue
            if url.startswith("//"):
                url = "https:" + url
            elif url.startswith("/"):
                base_url = "{0.scheme}://{0.netloc}".format(requests.utils.urlparse(current_url))
                url = base_url + url
            elif not url.startswith("http"):
                continue
            url = url.split("#")[0]

            # add to outlinks
            outlinks_formated.append(url)

            # Check if url has not been visited before
            if url not in visited_urls:
                urls.append(url)
                visited_urls.add(url)

        
        # save the pages outlinks 
        page_graph.graph_add(current_url, outlinks_formated)
        outlinks_formated.clear()