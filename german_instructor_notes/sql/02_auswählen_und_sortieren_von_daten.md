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

## Was ist eine Abfrage?
Eine Abfrage ist eine Anfrage nach Daten. Zum Beispiel: "Wie viele Zeitschriften abonniert unsere Bibliothek? Wenn wir eine Datenbank abfragen, können wir dieselbe Frage mit der Abfragesprache SQL in einer so genannten Anweisung stellen. Einige der nützlichsten Abfragen - diejenigen, die wir in diesem ersten Abschnitt vorstellen - werden verwendet, um Ergebnisse aus einer Tabelle zurückzugeben, die bestimmten Kriterien entsprechen.

## Meine erste Abfrage schreiben

Lasst uns damit beginnen, den DB Browser for SQLite und die Doaj-Artikel-Beispieldatenbank zu öffnen (siehe Setup). Wählt `Daten durchsuchen` und die Tabelle `article`. Die article Tabelle enthält Spalten oder Felder wie `Title`, `Authors`, `DOI`, `URL`, usw.

Lasst uns eine SQL-Abfrage schreiben, die nur die Spalte `Title` aus der Tabelle `articles` auswählt.

~~~
SELECT Title
FROM articles;
~~~

Wir haben die Wörter `SELECT` und `FROM` groß geschrieben, weil es sich um SQL-Schlüsselwörter oder auch Keywords handelt. Dies macht für den SQL-Interpreter keinen Unterschied, da es die Groß-/Kleinschreibung nicht berücksichtigt, aber es trägt zur Lesbarkeit bei und gilt daher als guter Stil.
Beachten Sie, dass einige Datenbanksysteme nach jeder SQL-Anweisung ein Semikolon `;` verlangen. Wenn wir mehr als eine Spalte auswählen, dann werden die verschiedenen Wertepaare zurückgegeben.

## Kommentare schreiben
Wenn die Abfragen komplexer werden, kann es nützlich sein, Kommentare hinzuzufügen. In SQL beginnen Kommentare mit `--`. Ein kommentierte Version der obigen Anfrage kann geschrieben werden als:

~~~
-- Spalte Title auswählen
SELECT * 
-- Aus der Tabelle articles
FROM articles;
~~~

Ihr könnt die Kommentarspalte nutzen, um Notizen für euch zu machen, die Abfrage zu umschreiben und um einzelne Zeilen auszukommentieren, wenn ihr Abfragen neu testet. Die Kommentare sind auch nützlich, wenn ihr eure Abfragen mit anderen teilt, damit diese sie leichter nachvollziehen können.

## Weitere SELECT Optionen
Wenn wir mehr Informationen wünschen, können wir direkt nach `SELECT` eine neue Spalte zu der Liste der Felder hinzufügen:

~~~
SELECT Title, Authors, ISSNs, Year
FROM articles;
~~~

Oder wir können alle Spalten in einer Tabelle mit dem Platzhalter `*` auswählen.

~~~
SELECT *
FROM articles;
~~~

## Eindeutige Werte

Es kann eine Situation eintreten, in der wir eindeutige Datensätze und nicht mehrere doppelte Datensätze abrufen müssen. Das Keyword `DISTINCT` wird nach `SELECT` verwendet, um doppelte Datensätze zu eliminieren und nur eindeutige Datensätze abzurufen. Lasst uns uns alle eindeutigen `ISSNs` in einer SQL-Abfrage zurückgeben.

~~~
SELECT DISTINCT ISSNs
FROM articles;
~~~

Wir können im Ergebnisfeld sehen, dass nun 51 statt der 1001 Zeilen zurückgegeben werden, da jede ISSN nur noch einmalig angezeigt wird.

~~~
SELECT DISTINCT ISSNs, Day, Month, Year
FROM articles;
~~~

## Sortierung

Wir können die Ergebnisse unserer Abfragen auch mit dem Keyword `ORDER BY` sortieren. Lassen Sie uns eine Abfrage erstellen, die die Tabelle der Artikel alphabetisch nach ISSNs sortiert, indem wir das Keyword `ASC` (ascending) in Verbindung mit `ORDER BY` verwenden. 

~~~
SELECT *
FROM articles
ORDER BY ISSNs ASC;
~~~

Das Keyword `ASC` weist uns an, sie in aufsteigender Reihenfolge zu ordnen. Stattdessen können wir `DESC` (descending) verwenden, um die absteigende Sortierung nach `First_Author` zu erhalten.

~~~
SELECT *
FROM articles
ORDER BY First_Author DESC;
~~~

`ASC` ist die Voreinstellung, durch Weglassen von `ASC` oder `DESC` sortiert SQLite also aufsteigend (ASC).

Wir können auch nach mehreren Feldern gleichzeitig und in verschiedene Richtungen sortieren. Wir können zum Beispiel nach `ISSNs` absteigend und dann nach `First_Author` aufsteigend in derselben Abfrage sortieren.

~~~
SELECT *
FROM articles
ORDER BY ISSNs DESC, First_Author ASC;
~~~

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
