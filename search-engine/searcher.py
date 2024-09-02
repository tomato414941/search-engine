from .preprocessor import preprocessor


class Searcher:
    def __init__(self, index, page_data):
        self.index = index
        self.page_data = page_data

    def search(self, query):
        processed_query = preprocessor.preprocess(query)
        if not processed_query:
            return []
        result_urls = set(self.index[processed_query[0]])
        for word in processed_query[1:]:
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
