```python
def plus_1(n, result):
  if n > 0:
    result +=1 
    print(result)
		plus_1(n-1, result)

plus_1(5, 0)

```

Copy python array `arr`

```arr[:]```

Launch simple python server
```
python3 -m http.server
```

Python set


## Math
- `round(num, digits)`

## Advanced
- **type hinting**


Particularity
Placeholder array. A Python trick. This used to be a problem in python2.x. Place holder [0]\*len(arr),  other items will change, when we index and change one of the values. Solution: Better use [0 for i in range(arr)]. Python 3.x this doesn’t seem to be a problem. 

## OOP
Creating a new class is equivalent of creating a new type in python
