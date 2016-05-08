# Why use `def __init__(self)`?

Let's say you have the following class:

```python
class Parrot:
    def talk(self):
        message = '{0} wants a cracker!'.format(self.name)
        print(message)
```

And we create an instance:

```python
polly = Parrot()
polly.name = "Polly"
polly.talk()
```

That works, right? But what happens if you forget to give the parrot a name?

```python
jimmy = Parrot()
jimmy.talk()
```

You should see this error: `AttributeError: Parrot instance has no attribute 'name'`

This is where the `__init__` method comes into play. When you create an instance, Python will first call the `__init__` method if it exists, which is often called the "initializer" or "constructor" since it used use to initialize the instance.

Update the class like so:

```python
class Parrot:
    def __init__(self, name="Happy"):
        self.name = name
    def talk(self):
        message = '{0} wants a cracker!'.format(self.name)
        print(message)
```

Now the default name is "Happy".

```python
johnny = Parrot()
johnny.talk()
```

Now the `talk` method should work fine.