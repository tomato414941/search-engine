class Searcher:
    def __init__(self, index):
        self.index = index

    def search(self, query):
        words = query.lower().split()
        if not words:
            return []
        results = set(self.index[words[0]])
        for word in words[1:]:
            results.intersection_update(set(self.index[word]))
        return list(results)
