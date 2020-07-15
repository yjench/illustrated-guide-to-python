# Non-probabilistic version of PageRank
# For advanced versions:
#   - https://en.wikipedia.org/wiki/PageRank#Python
#   - https://cs50.harvard.edu/ai/2020/projects/2/pagerank/

links = [('a', 'b'), ('a', 'c'), ('b', 'c')]

num_iters = 10  # 1
damping = 0.85  # 0.25, 1

# Collect all pages
pages = []
for t in links:
    pages.extend(t)
pages = sorted(set(pages))

# Construct corpus: {page: [targets of outbound links]}    
corpus = {page: [] for page in pages}
while links:
    page, target = links.pop()
    corpus[page].append(target)

# Initialize scores: {page: score}
scores = {page: 1 for page in pages}

# Set up temporary variable: {page: score to transfer to each target}
scores_to_transfer = {page: 0 for page in pages}

# Run PageRank iteration
for i in range(num_iters):
    # Logging
    if not i % 2:
        print(f'Iter {i}:')
        for page, score in scores.items():
            print(f'    {page} -> {score:.3f}')
    
    # Compute scores to transfer
    for page, score in scores.items():
        num_targets = len(corpus[page])        
        scores_to_transfer[page] = (damping * score / num_targets
                                    if num_targets != 0 else 0)
    
    # Update scores
    for page, targets in corpus.items():
        for target in targets:
            scores[page] -= scores_to_transfer[page]
            scores[target] += scores_to_transfer[page]

# Print final scores
print('-'*20)
print('Final scores:')
for page, score in scores.items():
    print(f'    {page} -> {score:.3f}')