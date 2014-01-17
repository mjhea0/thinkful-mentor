## Continue and Break

Loops are usually used to iterate over a block of code then exit after some condition is met. The `break` and `loop` statements alter that normal flow when specific conditions are met.

### Break

Break is used to terminate the loop. The program then moves to the next statement after the loop. 

#### First

```python
array = []

for letter in 'testing':
    if letter == 'i':
        break
    array.append(letter)

print array
```

#### Second

```python
num = 13                 
while num > 0:              
    print num,
    num = num - 1
    if num == 5:
        break
```

#### Third

```python
num = 13                 
while num > 0:              
    print num,
    num = num - 1
    if num == 5:
        for x in "STRING":
            if x == 'R':
                print "\nEXIT INNER LOOP"
                break
            print "\n"+x,
```

### Continue

Continue is used to skip the remaining code in a loop, which then returns the program to the beginning, contining on to the iteration.

#### First

```python
array = []

for letter in 'testing':
    if letter == 'i':
        continue
    array.append(letter)

print array
```

#### Second

```python
num = 13                 
while num > 0:              
    print num,
    num = num - 1
    if num == 5:
        continue
```

#### Third

```python
num = 13                 
while num > 0:              
    print num,
    num = num - 1
    if num == 5:
        for x in "STRING":
            if x == 'R':
                continue
            print "\n"+x,
        print ""
```

