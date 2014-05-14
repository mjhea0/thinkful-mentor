import sys
import os
import re

TAGS = sys.argv[1:]


def get_path():
    """grabs the user inputted path and verifies that it exists"""
    parsed = False
    while not parsed:
        path = raw_input("Input the working path to directory: ")
        if not os.path.exists(path):
            print "Sorry this path does not exist: {}".format(path)
        else:
            parsed = True
    return path


def get_files(file_path):
    """
    given a path as an argument, this returns all files in the directory,
    then adds the text of each file to a list
    """
    files = os.listdir(file_path)
    alltext = []
    for file in files:
        docs = os.path.join(file_path, file)
        with open(docs, "r") as f:
            fulltext = f.read()
            alltext.append(fulltext)
    return alltext


def get_search_expressions(TAGS):
    """given the TAGS, create regular expressions for searching"""
    searches = {}
    for tag in TAGS:
        searches[tag] = (re.compile(r'\b'+tag+r'\b', re.IGNORECASE))
    return searches


def key_counter(regex_searches, text):
    """counts the number of time each tag shows up"""
    for tag, search in regex_searches.iteritems():
        count = len(search.findall(text))
        print "The search term '{}' was counted {} times.".format(tag, count)
    print '*****************************'


def metadata(text):
    """returns all metadata from each file"""
    title_search = re.compile(r"""
                          (?:title:\s*) #look for 'title: ' in the original text.
                          (?P<title>        #then capture the following group which we'll
                                            #call title and can access with that name later

                          (                 #title consists of words, which are
                            (
                              \S*           #one or more non-white spaces
                              (\ )?         #followed by zero or 1 spaces
                                            # note how we have to use a slash to escape
                                            # the space character, since re.VERBOSE mode ignores
                                            # unescaped whitespace in your pattern.

                            )+              # title has 1 or more such words
                          )
                          (                 #and this set of words can optionally be followed
                            (\n(\ )+)       #by a new line character, plus a few spaces
                            (\S*(\ )?)*     #and then one or more additional words
                          )*                #and this * means the title can encompass
                          )""",             # however many extra lines we need
                          re.IGNORECASE | re.VERBOSE)  #note the #appearance of | above. 
                                            # This allows us to set multiple flags to our regex.
                                            # See: http://docs.python.org/dev/howto/regex.html#compilation-flags
    author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
    translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)

    title = re.search(title_search, text)
    author = re.search(author_search, text)
    translator = re.search(translator_search, text)
    if title:
        title = title.group('title')
    if author:
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    print '\n*****************************'
    print 'Title: ', title
    print 'Author: ', author
    print 'Translator: ', translator


def main():
    file_path = get_path()
    all_text = get_files(file_path)
    regex_searches = get_search_expressions(TAGS)
    for text in all_text:
        metadata(text)
        key_counter(regex_searches, text)


if __name__ == "__main__":
    main()