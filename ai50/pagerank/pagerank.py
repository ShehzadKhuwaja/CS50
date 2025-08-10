import os
import random
import re
import sys
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    transition_probability = {}
    total_html_pages =  len(corpus)
    non_damping_probability_per_page = (1 - damping_factor) / total_html_pages

    if len(corpus[page]) == 0:
        for html_page in corpus:
            transition_probability[html_page] = 1 / total_html_pages
        return transition_probability

    for key in corpus:
        transition_probability[key] = non_damping_probability_per_page

    html_pages = corpus[page]
    damped_pages_probability = damping_factor / len(html_pages)
    for page in html_pages:
        transition_probability[page] += damped_pages_probability

    return transition_probability 

    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    samples = []
    current_page = random.choice(list(corpus.keys()))
    samples.append(current_page)

    for _ in range(n - 1):
        p_distribution = transition_model(corpus, current_page, damping_factor)
        next_page = random.choices(list(p_distribution.keys()), list(p_distribution.values())) 
        samples.append(next_page[0])
        current_page = next_page[0]
    
    page_frequency = Counter(samples)
    page_frequency = dict(page_frequency)

    for key in page_frequency:
        page_frequency[key] /= n

    return page_frequency 

    
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_page_rank = {}
    for key in corpus:
        current_page_rank[key] = 1 / len(corpus)

    incident_links = incoming_links(corpus)
    not_converged = True
    while(not_converged):
        new_page_rank = {}
        for page in corpus:
            new_page_rank[page] = (1 - damping_factor) / len(corpus)
            damping_probability = 0
            for link in incident_links[page]:
                if len(corpus[link]) == 0:
                    damping_probability += current_page_rank[link] / len(corpus)
                else:
                    damping_probability += current_page_rank[link] / len(corpus[link])
            damping_probability *= damping_factor
            new_page_rank[page] += damping_probability
        
        not_converged = False
        for page in corpus:
            if abs(current_page_rank[page] - new_page_rank[page]) > 0.001:
                not_converged = True
                current_page_rank = new_page_rank 
                break

    for page in new_page_rank:
        new_page_rank[page] = round(new_page_rank[page], 3)
    
    return new_page_rank

    raise NotImplementedError

def incoming_links(corpus):
    """return a dict mapping pages to the links that are incident on them"""
    incident_link = {}

    for page in corpus:
        incident_link[page] = []

    empty_link_pages = []
    for page in corpus:
        if len(corpus[page]) == 0:
            empty_link_pages.append(page)

        for link in corpus[page]:
            incident_link[link].append(page)

    for page in incident_link:
        for empty_page in empty_link_pages:
            incident_link[page].append(empty_page)
    
    return incident_link


if __name__ == "__main__":
    main()
