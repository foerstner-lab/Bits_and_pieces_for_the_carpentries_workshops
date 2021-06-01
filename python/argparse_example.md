### argparse example

See [docs](https://docs.python.org/3/library/argparse.html) for more
information.


```python
number_1 = 10
number_2 = 30
result = number_1 + number_1
print(result)
```

```bash
$ python calc.py 
10
```

```calc.py
import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()

number_1 = 10
number_2 = 30
result = number_1 + number_1

print(result)
```

```bash 
$ python calc.py 
10
```

```bash
$ python calc.py -h
usage: calc.py [-h]

optional arguments:
  -h, --help  show this help message and exit
```

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number_1")
parser.add_argument("number_2")
args = parser.parse_args()

print(args)

# result = args.number_1 + args.number_2
# print(result)
```

```bash
$ python calc.py 1000 5000                                                                                         ~
Namespace(number_1='1000', number_2='5000')
```

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number_1")
parser.add_argument("number_2")
args = parser.parse_args()

result = args.number_1 + args.number_2
print(result)
```

```bash
$ python calc.py -h
usage: calc.py [-h] number_1 number_2

positional arguments:
  number_1
  number_2

optional arguments:
  -h, --help  show this help message and exit
```


```bash
$ python calc.py 1000 5000
10005000
```

```bash
python calc.py AAAA ZZZZ                                                                                         ~
AAAAZZZZ
```


```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number_1", type=int)
parser.add_argument("number_2", type=int)
args = parser.parse_args()

result = args.number_1 + args.number_2
print(result)
```


```bash
$ python calc.py 1000 5000
6000

```

```bash
$ python calc.py AAAA ZZZZ
usage: calc.py [-h] number_1 number_2
calc.py: error: argument number_1: invalid int value: 'AAAA'
```

```bash
$ python calc.py 1000 ZZZZ                                                                                           ~
usage: calc.py [-h] number_1 number_2
calc.py: error: argument number_2: invalid int value: 'ZZZZ'
```

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer" )
args = parser.parse_args()

result = args.number_1 + args.number_2
print(result)
```

```python
$ python calc.py -h
usage: calc.py [-h] number_1 number_2

positional arguments:
  number_1    An integer
  number_2    Another integer

optional arguments:
  -h, --help  show this help message and exit
```

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer" )
add_argument("--multi", default=False, action="store_true")
args = parser.parse_args()

result = args.number_1 + args.number_2
print(result)
```

```bash
$ python calc.py -h                                                                                                ~
usage: calc.py [-h] [--multi] number_1 number_2

positional arguments:
  number_1    An integer
  number_2    Another integer

optional arguments:
  -h, --help  show this help message and exit
  --multi
```

```bash
$ python calc.py 1000 5000
6000
Namespace(multi=False, number_1=1000, number_2=5000)
```

```bash
$ python calc.py --multi 1000 5000
6000
Namespace(multi=True, number_1=1000, number_2=5000)
```

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer" )
parser.add_argument("--multi", default=False, action="store_true")
args = parser.parse_args()

if args.multi:
    result = args.number_1 * args.number_2
else:
    result = args.number_1 + args.number_2

print(result)
```

```bash
$ python calc.py 1000 5000
6000
```

```bash
$ python calc.py --multi 1000 5000
5000000
```

```bash
$ python calc.py --operation sum 1000 5000
6000
```

```bash
$ python calc.py 1000 5000
6000
```

```bash
$ python calc.py --operation sum 1000 5000
6000
```

```bash
$ python calc.py --operation mult 1000 5000
5000000
```

```bash
$ python calc.py --operation div 1000 5000
0.2
```

```bash
$ python calc.py --operation sub 1000 5000
-4000
```

```bash
$ python calc.py --operation blub 1000 5000
usage: calc.py [-h] [--operation {sum,mult,div,sub}] number_1 number_2
calc.py: error: argument --operation: invalid choice: 'blub' (choose from 'sum', 'mult', 'div', 'sub')
```

TO BE CONTINUED
