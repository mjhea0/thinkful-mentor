import os
import sys
import re

# path to the directory housing text docs as command line argument
directory = sys.argv[1]

# # create dict of keywords with a dict comprehension
# keywords = {
#     keyword: re.compile(r'\b' + keyword + r'\b') for keyword in sys.argv[2:]
# }


keywords = {}
for keyword in sys.argv[2:]:
    keywords[keyword] = keyword

# regular expressions
title_search = re.compile(
    r'(?:title:\s*)(?P<title>((\S*( )?)+)' +
    r'((\n(\ )+)(\S*(\ )?)*)*)',
    re.IGNORECASE
)
author_search = re.compile(
    r'(author:)(?P<author>.*)',
    re.IGNORECASE
)
translator_search = re.compile(
    r'(translator:)(?P<translator>.*)',
    re.IGNORECASE
)
illustrator_search = re.compile(
    r'(illustrator:)(?P<illustrator>.*)',
    re.IGNORECASE
)

for file_name in (os.listdir(directory)):
    if file_name.endswith('.txt'):
        file_name_path = os.path.join(directory, file_name)
        # search individual files
        with open(file_name_path, 'r') as f:
            full_text = f.read()
        # search individual file for text that matches regex
        title = re.search(title_search, full_text)
        if title:
            title = title.group('title')
        author = re.search(author_search, full_text)
        if author:
            author = author.group('author')
        translator = re.search(translator_search, full_text)
        if translator:
            translator = translator.group('translator')
        illustrator = re.search(illustrator_search, full_text)
        if illustrator:
            illustrator = illustrator.group('illustrator')
        # outputs
        print "---" * 25
        print "Here's the info for {}:".format(file_name)
        print "Title: {}".format(title)
        print "Author(s): {}".format(author)
        print "Translator(s): {}".format(translator)
        print "Illustrator(s): {}".format(illustrator)
        print "\n# ---- KEYWORD REPORT ---- #\n\n"
        for keyword in keywords:
            print keyword
            print "'{0}': {1}".format(
                keyword,
                len(re.findall(keywords[keyword], full_text))
                )
        print "\n"
