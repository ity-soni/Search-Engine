import os
import re
import string


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    files=[]
    cwd=os.getcwd()
    for path,i,file_lst in os.walk(root):
        for f in file_lst:
            files.append(cwd+'/'+path+'/'+f)
    return files


def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w.lower() for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    # words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    page='<html>\n  <body>\n   <h2>Search results for <b>'+' '.join(terms)+'</b> in '+str(len(docs))+' files</h2>\n'
    for doc in docs:
        with open(doc) as fd:
            lines=fd.readlines()
            count=0
            returnlst=[]
            for line in lines:
                found=False
                for term in terms:
                    regex=re.compile(term,re.I)
                    s=re.search(regex,line)
                    if s:
                        found=True
                        line=regex.sub('<b>'+s[0]+'</b>',line)
                if found==True:
                    count+=1
                    returnlst.append(line)
                if count==2:
                    break
            page+='        <p><a href="file://'+doc+'">'+doc+'</a><br>'+'<br>'.join(returnlst)+'<br><br>\n'
    page+='...\n</body>\n</html>'
    return page


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

