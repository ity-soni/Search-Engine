# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    mapping=htable(4011)
    for fileName in files:
        text=get_text(fileName)
        text=words(text)
        for word in text:
            val=htable_get(mapping,word)
            if val==None:
                val=fileName
            else:
                if type(val)!=list:
                    val=[val]
                if fileName not in val:
                    val.append(fileName)
            mapping=htable_put(mapping,word,val)
    return mapping
        
    
def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    search_list=set(files)
    for term in terms:
        k_idx=bucket_indexof(index,term)
        if k_idx!=None:
            search_list=search_list.intersection(set(htable_get(index,term)))
        else:
            search_list=set()
    return search_list
    
    
    