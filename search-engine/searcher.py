class Searcher:
    def __init__(self, index, page_data):
        self.index = index
        self.page_data = page_data

    def search(self, query):
        words = query.lower().split()
        if not words:
            return []
        result_urls = set(self.index[words[0]])
        for word in words[1:]:
            result_urls.intersection_update(set(self.index[word]))

        results = []
        for url in result_urls:
            results.append(
                {
                    "url": url,
                    "title": self.page_data[url]["title"],
                    "snippet": self.page_data[url]["snippet"],
                    "last_crawled": self.page_data[url]["last_crawled"],
                }
            )
        return results
