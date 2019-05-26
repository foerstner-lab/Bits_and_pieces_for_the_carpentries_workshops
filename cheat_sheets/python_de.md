# Python

## Variablen und Wertezuweisung (Assignment)

```
name = "Darwin"
``` 

## Einfach Datentypen

str - Zeichenkette (String)
int - Ganzzahl (Integer)
float - Gleitkommazahl (Floating point number)
bool - Boolesche Werte (Boolean)

## Container-Datentypen

### Listen 

```
names = ["Noether", "Darwin", "Lovelace"]
``` 

Elemente werden durch den Index adressiert - z.B: `names[0]`

### Dictionaris

- Schlüssel/Werte-Paar

```
person_and_birth_years = {"Noether": 1882, "Darwin": 1809, "Lovelace": 1815}
```
- Werte werden über die Schlüssel adressiert - z.B: `person_and_birth_years["Noether"]`

## Operatoren
- `+`, `-`, `*`, `/`
- `==`, `!=`, `<`, `>`, `=<`, `=>`
- `not`, `and`, `or`

## for-Schleifen (for-Loops)

``` 
for <Variable> in <Liste/Interable>:
    <Auszuführender Block>
``` 

## Bedingte Anweisung (Conditionals)
``` 
if <Bedingung>:
    <Auszuführender Block>
``` 


``` 
if <Bedingung>:
    <Auszuführender Block>
else:
    <Auszuführender Block>
``` 

``` 
if <Bedingung 1>:
    <Auszuführender Block>
elif <Bedingung 2>:

else:
    <Auszuführender Block>
``` 




## Kommentare

- Alle rechts eine `#` steht wird nicht interpretiert

## Bibliotheken einbinden

``` 
import csv
```

``` 
import urllib.request
[...]
urllib.request.urlopen

```

``` 
import pandas as pd
``` 

# Funktionen und Methoden nutzen

## Funktionen

Funktionaufruf durch runde klammern 

- Beispiel:
  - `print("Hello World!")`
  - `type(counter)`
  - len([5, 23, 52 ])

## Methoden

Funktionen die an Objekte gebunden sind

- `name.upper()`
- `name.replace("und", "oder")`
