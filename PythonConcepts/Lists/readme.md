
## Creating a empty list
```
a = []
```

## Creating a list with values
```
b=[1,2,3]
c=["a","b","c"]
d=[1,"a",3.0]
print(a)
print(b)
print(c)
print(d)
```

**Output**
```
[]
[1, 2, 3]
['a', 'b', 'c']
[1, 'a', 3.0]
```

## Append element in the end
```
a.append(1)
a.append('x')
a.append(3.0)
print(a)
```
**Output**
```
[1, 'x', 3.0]
```
## Insert element at certain index
```
a.insert(2,'xx')
print(a)
```

**Output**
```
[1, 'x', 'xx', 3.0]
```
## Extending a list
```
b.extend(c)
print(b)
```

**Output**
```
[1, 2, 3, 'a', 'b', 'c']
```

## Remove an element(value) from list
```
b=[1,2,3,4,5,6]
b.remove(4
print(b)
```

**Output**
```
[1, 2, 3, 5, 6]
```

## Remove last element from list
```
b=[1,2,3,4,5,6]
b.pop()
print(b)
```

**Output**
```
[1, 2, 3, 4, 5]
```

## Remove element at specific index from list
```
b=[1,2,3,4,5,6]
b.pop(0)
print(b)
```

**Output**
```
[2, 3, 4, 5, 6]
```