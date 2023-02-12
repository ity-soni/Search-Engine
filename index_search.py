from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    mapping={}
    for fileName in files:
        text=get_text(fileName)
        text=words(text)
        for word in set(text):
            if word not in mapping:
                mapping[word]=set()
            mapping[word].add(fileName)
    return mapping           


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    search_list=set()
    for term in terms:
        if term in index:
            if search_list:
                search_list=search_list.intersection(index[term])
            else:
                search_list=index[term]
    return search_list.intersection(set(files))
