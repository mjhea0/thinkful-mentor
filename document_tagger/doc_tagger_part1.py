import re
import sys

from pg_sample_texts import DIV_COMM, MAG_CART

documents = [DIV_COMM, MAG_CART]

keywords = {}
for keyword in sys.argv[1:]:
    keywords[keyword] = re.compile(r'\b' + keyword + r'\b', re.IGNORECASE)

title_search = re.compile(r'(title:\s*)(?P<title>[a-zA-Z, \n]* \s)', re.IGNORECASE)
title_search = re.compile(r'(?:title:\s*)(?P<title>((\S*(\ )?)+)((\n(\ )+)(\S*(\ )?)*)*)',re.IGNORECASE | re.VERBOSE)
author_search = re.compile(r'(author:*)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:*)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:*)(?P<illustrator>.*)', re.IGNORECASE)

for document_number, document in enumerate(documents):

    title = re.search(title_search, document).group('title')
    author = re.search(author_search, document)
    translator = re.search(translator_search, document)
    illustrator = re.search(illustrator_search, document)

    if author:
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')

    print "\nDocument #: {}".format(document_number+1)
    print "--------------"
    print "Title: {}".format(title)
    print "Author(s): {}".format(author)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}".format(illustrator)
    print "Keywords:"
    for keyword in keywords:
        keyword_count = len(re.findall(keywords[keyword], document))
        print " - '{0}': {1}\n".format(keyword, keyword_count)