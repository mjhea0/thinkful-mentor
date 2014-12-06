import re

txt = """
title: abcd author: jumpa lahiri
title: defg author: dexter filkin
title: pqxr author: ernest hemingway
"""

for (title, author) in re.findall(r'title: (.*?) author: (.*)', txt):
    print title
    print author