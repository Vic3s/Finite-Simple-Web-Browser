from database_helper import insert_singel_page_outlinks

def graph_add(url, hyperlinks):
    page_outlinks_object = {'url': url, 'outlinks': hyperlinks}

    insert_singel_page_outlinks(page_outlinks_object)