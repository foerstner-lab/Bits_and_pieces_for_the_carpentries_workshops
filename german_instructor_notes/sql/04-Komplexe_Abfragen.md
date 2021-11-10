---
Titel: "Ordnen"
Unterricht: 15
Übungen: 0
Fragen:
- "Wie ist die Reihenfolge der Ausführung bei SQL-Abfragen?
Ziele:
- "Verstehen, wie man Abfragen erstellt, und die Reihenfolge, in der die Teile erstellt werden.
Schlüsselpunkte:
- "Abfragen haben oft die Struktur: SELECT data FROM table WHERE bestimmte Kriterien vorhanden sind". 
---

## Reihenfolge der Ausführung

Wir haben nun schon einige Abfragen an den SQL-Interpeter gestellt. Schauen wir uns einmal genau an 
wie dieser unsere Abfragen verarbeitet. Nehmen wir an, wir hätten die folgende Frage:

~~~
SELECT Title, Authors
FROM articles
WHERE ISSNs = '2056-9890'.
ORDER BY First_Author ASC;
~~~

Interessant an dieser Abfrage ist, dass wir nicht unbedingt die Spalte `First_Author` in unseren Ergebnissen anzeigen müssen, um nach ihr zu sortieren. 
Das können wir tun, weil die Sortierung früher durch den SQL-Interpreter erfolgt.

> ## Der Interpreter macht das im Grunde genommen:
> 1. Steuert die Tabelle `articles` an
> 1. Filtert nach den Bedinungen zu dem Keyword `WHERE`
> 2. Sortiert die Ergebnisse nach `ORDER BY`
> 3. Gibt die angeforderten Spalten aus der Zeile SELECT zurück

Wir können uns also merken, dass die `SELECT`-Zeile immer als letztes ausgeführt wird und die Bedinungen, die 
wir nach FROM stellen auf die gesamte Tabelle angewandt werden.

## Komplexe Abfragen

Je komplexer unsere Anforderungen werden, desto länger werden unsere Zeilen. 
Schauen wir uns einen Weg an, wie wir unsere Abfrage abkürzen können. Faulheit ist eine Tugend! 

Betrachten wir die folgende Abfrage:

~~~
SELECT *
FROM articles
WHERE (ISSNs = '2076-0787') OR (ISSNs = '2077-1444') OR (ISSNs = '2056-9890');
~~~

Wir müssen diese Abfrage nicht nur lange tippen, sie wird auch immer schwerer zu lesen. 
Hier können wir das KEYWORD `IN` verwenden, um die Abfrage zu verbessern und lesbarer zu machen.
`IN` wird verwendet, wenn wir eine Spalte mit mehr als einem Wert vergleichen wollen und ist vergleichbar mit einer `OR`-Bedingung

~~~
SELECT *
FROM articles
WHERE (ISSNs IN ('2076-0787', '2077-1444', '2056-9890'));
~~~
