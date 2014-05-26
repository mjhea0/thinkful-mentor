# Serialization with Pickle and JSON

## Serialization

Process of converting a data structure into a format that can be stored (file or cache) or transmitted, which can then be deserialized later. Python uses the [Pickle](https://wiki.python.org/moin/UsingPickle) and [JSON](http://docs.python.org/2/library/json) modules for serialization and deseralization.

*JSON vs SimpleJSON?*

## Pickle

### Saving to a file

```sh
>>> import pickle
>>> sample_dict = {'Name': 'Michael', 'Age': 30, 'Class': 'First'}
>>> with open('sample_dict.pickle','wb') as file:
...     pickle.dump(sample_dict, file)
...
>>>
```

 > The `dump()` function takes a serializeable data structure as an argument (a dictionary, in this case), then serializes it into binary.

### Loading from a file

```sh
>>> import pickle
>>> with open('sample_dict.pickle','rb') as file:
...     my_dict = pickle.load(file)
...
>>> my_dict
{'Age': 30, 'Name': 'Michael', 'Class': 'First'}
>>>
```

> The `load()` function takes an object (sample_dict.pickle), and then creates/returns a new object (my_dict) from the serialized data.

### Saving/Loading from memory

```sh
>>> import pickle
>>> sample_dict = {'Name': 'Michael', 'Age': 30, 'Class': 'First'}
>>> in_memory = pickle.dumps(sample_dict)
>>> type(in_memory)
<type 'str'>
>>> new_dict = pickle.loads(in_memory)
>>> type(new_dict)
<type 'dict'>
>>> new_dict
{'Age': 30, 'Name': 'Michael', 'Class': 'First'}
>>> new_dict == sample_dict
True
>>>
```

## JSON

### Saving to a JSON file

```sh
>>> import json
>>> import codecs
>>> sample_dict = {'Name': 'Michael', 'Age': 30, 'Class': 'First'}
>>> with codecs.open('json-file.json','w', encoding='utf-8') as file:
...    json.dump(sample_dict,file,indent=4)
...
>>>
```

### Loading from a JSON file

```sh
>>> import json
>>> import codecs
>>> with codecs.open('json-file.json','r', encoding='utf-8') as file:
...    json_data = json.load(file)
...
>>> type(json_data)
<type 'dict'>
>>> json_data
{u'Age': 30, u'Name': u'Michael', u'Class': u'First'}
>>> sample_dict = {'Name': 'Michael', 'Age': 30, 'Class': 'First'}
>>> json_data == sample_dict
True
>>>
```
