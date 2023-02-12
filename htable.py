"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for i in range(nbuckets)]


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if type(o)==int:
        return o
    elif type(o)==str:
        h=ord(o[0])
        for i in o[1:]:
            h=h*31+ord(i)
        return h
    else:
        return None

    
def get_bucket_id(table,key):
    if hashcode(key):
        return hashcode(key)%len(table)
    
    
def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    bucket=table[get_bucket_id(table,key)]
    for i in range(len(bucket)):
        if bucket[i][0]==key:
            return i
    return None


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    hindex=get_bucket_id(table,key)
    if hindex!=None:
        k_idx=bucket_indexof(table,key)
        if k_idx!=None:
            table[hindex][k_idx]=(key,value)
        else:
            table[hindex].append((key,value))
    return table


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    hindex=get_bucket_id(table,key)
    if hindex!=None:
        k_idx=bucket_indexof(table,key)
        if k_idx!=None:
            return table[hindex][k_idx][1]
    return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    s=''
    for i in range(len(table)):
        s+=str(i).rjust(4,'0')+'->'
        for j in table[i]:
            s+=str(j[0])+':'+str(j[1])+', '
        s=s.strip(', ')+'\n'
    return s
        

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    s='{'
    for i in range(len(table)):
        if table[i]==[]:
            continue
        for j in table[i]:
            s+=str(j[0])+':'+str(j[1])+', '
    s=s.strip(', ')
    s+='}'
    return s
    
    
