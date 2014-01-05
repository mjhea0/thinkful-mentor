# Proper shebang in Python

### What's the difference between `#!/usr/bin/python` and `#!/usr/bin/env python`?

1. `#!/usr/local/bin/python` specifies the *exact* location of Python on your machine, which will be used to interpret the remainder of the script.
2. `#!/usr/bin/env python` uses the version of Python that is *default* in your current enviornment (by searching the PATH), making that interpret the rest of the script. "env" executes the first thing it finds in the PATH env variable. 

### What does this mean?

The latter way is preferred since it's not dependent on a particular installation. In other words, if you use the same script on a different machine, `#!/usr/bin/env python` will find the correct path to Python; it's independent of where Python is located.

> I personally only add a this first line when I want to run a Python script as an executable - e.g., `./hello.py` vs `python ./hello.py`

### PATH

To find the location of Python on your machine:

#### Windows

```
>>> import os
>>> import sys
>>> os.path.dir
'C:\\Python27'
```

#### Mac

