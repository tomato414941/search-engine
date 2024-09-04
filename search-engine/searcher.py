from collections import defaultdict

from .preprocessor import preprocessor


class Searcher:
    def __init__(self, index, idf, page_data, pagerank):
        self.index = index
        self.idf = idf
        self.page_data = page_data
        self.pagerank = pagerank

    def search(self, query):
        processed_query = preprocessor.preprocess(query)
        if not processed_query:
            return []

        scores = defaultdict(float)
        for word in processed_query:
            if word in self.index:
                idf = self.idf[word]
                for url, tf in self.index[word].items():
                    scores[url] += tf * idf

        # Combine TF-IDF score with PageRank
        for url in scores:
            scores[url] = 0.5 * scores[url] + 0.5 * self.pagerank.get(url, 0)

        ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        results = []
        for url, score in ranked_results:
            results.append(
                {
                    "url": url,
                    "title": self.page_data[url]["title"],
                    "snippet": self.page_data[url]["snippet"],
                    "last_crawled": self.page_data[url]["last_crawled"],
                    "score": score,
                    "pagerank": self.pagerank.get(url, 0),
                }
            )

        return results
