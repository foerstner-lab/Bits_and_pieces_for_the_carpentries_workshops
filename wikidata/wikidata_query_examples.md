# Wikidata Query Beispiele

**Bibliotheken**
```
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q7075.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } 
}
```

**Karte von Bibliotheken**
```
#defaultView:Map
SELECT distinct * WHERE {
  ?item wdt:P31/wdt:P279* wd:Q7075;
        wdt:P625 ?geo .
}
```

**Journal Beispiel**
```
SELECT ?item ?itemLabel ?journalLabel
WHERE 
{
  ?item wdt:P31 wd:Q13442814.
  ?item wdt:P50 wd:Q18921408.
  ?item wdt:P1433 ?journal.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }
}
```

**Russische Poet:innen**
```
SELECT ?item ?itemLabel ?place ?placeLabel
WHERE 
{
  ?item wdt:P31 wd:Q5.
  ?item wdt:P106 wd:Q49757.
  ?item wdt:P19 ?place.
  ?place wdt:P17 wd:Q159.
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
```
SELECT ?item ?itemLabel ?place ?placeLabel ?coord
WHERE 
{
  ?item wdt:P31 wd:Q5.
  ?item wdt:P106 wd:Q49757.
  ?item wdt:P19 ?place.
  ?place wdt:P17 wd:Q159.
  ?place wdt:P625 ?coord
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
**Chemikalien Beispiel**
```
SELECT ?item ?itemLabel WHERE {
  
  ?item wdt:P31 wd:Q11173, wd:Q12140.
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }
}
```
```
SELECT ?item ?itemLabel ?struc ?formula

WHERE {
  
  ?item wdt:P31 wd:Q11173, wd:Q12140.
  ?item wdt:P117 ?struc.
  ?item wdt:P274 ?formula
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }
  
}
```
```
SELECT ?item ?itemLabel ?formula ?mass ?struc

WHERE {
  
  ?item wdt:P31 wd:Q11173, wd:Q12140.
  ?item wdt:P117 ?struc.
  ?item wdt:P274 ?formula.
  ?item wdt:P2067 ?mass.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }
  
}

ORDER BY DESC(?mass)
LIMIT 10
```
**Menschen, die in Berlin geboren sind - Nach Jahr gefiltert**
```
SELECT ?item ?itemLabel ?dob
WHERE 
{
  ?item wdt:P31 wd:Q5.
  ?item wdt:P19 wd:Q64.
  ?item wdt:P569 ?dob.
  
  FILTER(YEAR(?dob) = 1970)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
