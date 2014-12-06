""" Verbose regex demo """

import re

phone = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
phone2 = re.compile(r"""
    (\d{3})             # 3 digit area code
    \D*                 # any separator
    (\d{3})             # 3 digit phone
    \D*                 # any separator
    (\d{4})             # 4 digit phone
    \D*                 # any separator
    (\d*)               # extension
    $                   # right anchor
    """, re.VERBOSE)

print re.findall(phone, '215-555-1212')
print re.findall(phone2, '215-555-1212-9')


author_search = re.compile(r'(author:)(?P<author>.*)')
author_search2 = re.compile(r'''
    (author:)           # opening tag
    (?P<author>.*)      # save the author data
    ''', re.VERBOSE)
print re.findall(author_search2, "author: Sam Halperin")
