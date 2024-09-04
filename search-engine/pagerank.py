import numpy as np


def calculate_pagerank(links, damping_factor=0.85, num_iterations=100, tolerance=1e-8):
    num_pages = len(links)
    ranks = np.ones(num_pages) / num_pages

    # Create adjacency matrix
    adjacency_matrix = np.zeros((num_pages, num_pages))
    for i, outlinks in enumerate(links.values()):
        for outlink in outlinks:
            if outlink in links:  # Only consider links to pages we've crawled
                j = list(links.keys()).index(outlink)
                adjacency_matrix[j, i] = 1

    # Normalize adjacency matrix
    column_sums = adjacency_matrix.sum(axis=0)
    column_sums[column_sums == 0] = 1  # Avoid division by zero
    adjacency_matrix = adjacency_matrix / column_sums

    for _ in range(num_iterations):
        prev_ranks = ranks.copy()
        ranks = (
            1 - damping_factor
        ) / num_pages + damping_factor * adjacency_matrix.dot(ranks)
        if np.abs(ranks - prev_ranks).sum() < tolerance:
            break

    return dict(zip(links.keys(), ranks))
