import nltk
import sys
import os
import string
import collections
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)
    
    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)
    
    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    content = {}
    for file in os.listdir(directory):
        with open(os.path.join(directory, file)) as f:
            content[file] = f.read()
    return content
    raise NotImplementedError


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # code is similar to tf0.py in notes 
    content = [word for word in nltk.word_tokenize(document.lower()) if word not in string.punctuation and word not in nltk.corpus.stopwords.words("english")]
    return content
    raise NotImplementedError


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    keys = set()
    for document in documents:
        items = set(documents[document])
        keys = keys.union(items)
    
    # NUMOFDOCUMENT(WORD) 
    NDC = dict.fromkeys(keys, 0)
    for key in keys:
        for document in documents:
            if key in documents[document]:
                NDC[key] += 1

    for word in NDC:
        NDC[word] = math.log(len(documents) / NDC[word])

    return NDC
    raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    top_files = dict.fromkeys(files.keys(), 0)
    for word in query:
        for file in files:
            if word in files[file]:
                top_files[file] += collections.Counter(files[file])[word] * idfs[word]
    top_files = sorted(top_files, key=lambda item: top_files[item], reverse=True)
    top_files = top_files[:n]
    return top_files
    raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    top_sentences = dict.fromkeys(sentences)
    for sentence in sentences:
        # matching word measure (mwm)
        mwm = 0
        # query term density (qtd)
        qtd = 0
        for word in query:
            if word in sentences[sentence]:
                mwm += idfs[word]
                qtd += 1 / len(sentences[sentence])
        top_sentences[sentence] = (mwm, qtd)
    top_sentences = sorted(top_sentences, key=lambda item: (top_sentences[item][0], top_sentences[item][1]), reverse=True)
    return top_sentences[:n]

    raise NotImplementedError


if __name__ == "__main__":
    main()
