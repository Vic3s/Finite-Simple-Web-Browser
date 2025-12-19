
def pagerank(graph, damping_factor=0.85, max_iterations=100):
    # Get all urls in a set
    page_nodes = set(graph.keys())

    for links in graph.values():
        page_nodes.update(links)

    count_nodes = len(page_nodes)

    # Create the initial page rank vector
    pagerank_vector = {url: 1.0 / count_nodes for url in page_nodes}

    # Get all dngling nodes
    dangling_nodes = [node for node in page_nodes if node not in graph or len(graph[node]) == 0]

    for itr in range(max_iterations):
        new_pagerank_vector = {}

        # Sum of of pageranks for all dangling nodes
        dangling_sum = damping_factor * sum(pagerank_vector[node] for node in dangling_nodes) / count_nodes
        for url in page_nodes:
            rank =  (1.0 - damping_factor) / count_nodes
            rank += dangling_sum
            for node in graph:
                if url in graph[node]:
                    outlinks_degree = len(graph[node])
                    rank += damping_factor * pagerank_vector[node] / outlinks_degree
            new_pagerank_vector[url] = rank
            
        pagerank_vector = new_pagerank_vector

        # Round to the 6th decimal
        for url in page_nodes:
            pagerank_vector[url] = round(pagerank_vector[url], 6)

        return(pagerank_vector)
