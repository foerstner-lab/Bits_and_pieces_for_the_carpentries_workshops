---
Titel: "Auswählen und Sortieren von Daten".
Unterricht: 15
Übungen: 5
Fragen:
- "Was ist eine Frage?"
- "Wie fragt man Datenbanken mit SQL ab?"
- "Wie rufen Sie eindeutige Werte in SQL ab?"
- "Wie sortieren Sie Ergebnisse in SQL?
Ziele:
- "Verstehen, wie SQL zur Abfrage von Datenbanken verwendet werden kann".
- "Verstehen, wie man Abfragen erstellt, unter Verwendung von SQL-Schlüsselwörtern wie `DISTINCT` und `ORDER BY`"
Schlüsselpunkte:
- "SQL ist ideal für die Abfrage von Datenbanken".
- "SQL-Abfragen haben eine grundlegende Abfragestruktur, die mit `SELECT` Feld FROM Tabelle mit zusätzlichen Schlüsselwörtern und Kriterien beginnt, die verwendet werden können. 
---

## Was ist eine Anfrage?
Eine Abfrage ist eine Frage oder Anfrage nach Daten. Zum Beispiel: "Wie viele Zeitschriften abonniert unsere Bibliothek? Wenn wir eine Datenbank abfragen, können wir dieselbe Frage in einer gemeinsamen Sprache namens Structured Query Language oder SQL in einer so genannten Anweisung stellen. Einige der nützlichsten Abfragen - diejenigen, die wir in diesem ersten Abschnitt vorstellen - werden verwendet, um Ergebnisse aus einer Tabelle zurückzugeben, die bestimmten Kriterien entsprechen.


## Meine erste Abfrage schreiben

Lasst uns damit beginnen, den DB Browser for SQLite und die Doaj-Artikel-Beispieldatenbank zu öffnen (siehe Setup). Wählt `Daten durchsuchen` und die Tabelle `article`. Die article Tabelle enthält Spalten oder Felder wie `Title`, `Authors`, `DOI`, `URL`, usw.

Lasst uns eine SQL-Abfrage schreiben, die nur die Spalte `Title` aus der Tabelle `articles` auswählt.

~~~
SELECT Title
FROM articles;
~~~
{: .sql}

Wir haben die Wörter `SELECT` und `FROM` groß geschrieben, weil es sich um SQL-Schlüsselwörter handelt. Dies macht für den SQL-Interpreter keinen Unterschied, da es die Groß-/Kleinschreibung nicht berücksichtigt, aber es trägt zur Lesbarkeit bei und gilt daher als guter Stil.

Wenn wir mehr Informationen wünschen, können wir direkt nach `SELECT` eine neue Spalte zu der Liste der Felder hinzufügen:


~~~
SELECT Title, Authors, ISSNs, Year
FROM articles;
~~~
{: .sql}

Oder wir können alle Spalten in einer Tabelle mit dem Platzhalter `*` auswählen.

~~~
SELECT *
FROM articles;
~~~
{: .sql}

## Eindeutige Werte

Es kann eine Situation eintreten, in der Sie eindeutige Datensätze und nicht mehrere doppelte Datensätze abrufen müssen. Das SQL-Schlüsselwort `DISTINCT` wird nach `SELECT` verwendet, um doppelte Datensätze zu eliminieren und nur eindeutige Datensätze abzurufen. Lassen Sie uns alle eindeutigen `ISSNs` in einer SQL-Abfrage zurückgeben.

~~~
SELECT DISTINCT ISSNs
FROM articles;
~~~
{: .sql}

Beachten Sie, dass einige Datenbanksysteme nach jeder SQL-Anweisung ein Semikolon `;` verlangen. Wenn wir mehr als eine Spalte auswählen, dann werden die verschiedenen Wertepaare zurückgegeben.

~~~
SELECT DISTINCT ISSNs, Day, Month, Year
FROM articles;
~~~
{: .sql}

## Sortierung

Wir können die Ergebnisse unserer Abfragen auch mit dem Schlüsselwort `ORDER BY` sortieren. Lassen Sie uns eine Abfrage erstellen, die die Tabelle der Artikel alphabetisch nach ISSNs sortiert, indem wir das Schlüsselwort `ASC` in Verbindung mit `ORDER BY` verwenden. 

~~~
SELECT *
FROM articles
ORDER BY ISSNs ASC;
~~~
{: .sql}

Das Schlüsselwort `ASC` weist uns an, sie in aufsteigender Reihenfolge zu ordnen. Stattdessen können wir `DESC` verwenden, um die absteigende Sortierung nach `First_Author` zu erhalten.

~~~
SELECT *
FROM articles
ORDER BY First_Author DESC;
~~~
{: .sql}

`ASC` ist die Voreinstellung, durch Weglassen von `ASC` oder `DESC` sortiert SQLite also aufsteigend (ASC).

Wir können auch nach mehreren Feldern gleichzeitig und in verschiedene Richtungen sortieren. Wir können zum Beispiel nach `ISSNs` absteigend und dann nach `First_Author` aufsteigend in derselben Abfrage sortieren.

~~~
SELECT *
FROM articles
ORDER BY ISSNs DESC, First_Author ASC;
~~~
{: .sql}

> ## Herausforderung
> Schreibe eine Abfrage, die `Titel`, `Erster_Autor`, `ISSNs` und `Zitat_Zählung` aus
> die Tabelle der Artikel, geordnet nach dem oben zitierten Artikel und alphabetisch nach Titel.
>
> > ## Lösung
> > ~~~
> > SELECT Title, First_Authot, ISSNs, Citation_Count
> > FROM articles
> > ORDER BY Citation_Count DESC, Titel ASC;
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}
