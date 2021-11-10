---
Titel: "Werte aggregieren & berechnen"
Unterricht: 15
Übungen: 5
Fragen:
- "Wie können wir Werte in SQL aggregieren?"
- "Kann SQL für Berechnungen verwendet werden?"
Ziele:
- "Verwende SQL-Funktionen wie `AVG` in Kombination mit `Group By`, um Werte zu aggregieren und Ergebnisse für Berichte zurückzugeben.
- "Berechnungen für Felder mit SQL durchführen."
Schlüsselpunkte:
- "SQL kann für Berichtszwecke verwendet werden."
- "Abfragen können arithmetische Operationen auf Feldwerten durchführen."
---

## Aggregation

SQL enthält Funktionen, mit denen Sie Berechnungen mit Daten in Ihrer Datenbank durchführen können. Einige der gebräuchlichsten Funktionen sind `MAX, MIN, AVG, COUNT, SUM', und das werden sie auch: 
- `MAX`: findet den maximalen Wert in einem Feld
- `MIN`: findet den minimalen Wert in einem Feld
- `AVG`: findet den Durchschnittswert eines Feldes
- `COUNT`: zählt die Anzahl der Werte in einem Feld und stellt die Summe dar
- `SUM`: addiert die Werte in einem Feld und stellt die Summe dar

Nehmen wir an, wir wollen den durchschnittlichen Wert von `Citation_Count` für jede `ISSN` erhalten. Wir können `AVG` und `GROUP BY` in einer Abfrage verwenden:

~~~
SELECT ISSNs, AVG(Citation_Count)
FROM articles
GROUP BY ISSNs;
~~~

`GROUP BY` wird von SQL verwendet, um identische Daten in Gruppen zusammenzufassen. In diesem Fall ordnen wir alle `Zitationen` nach `ISSNs` an. `AVG` wirkt auf die `Citation_Count` in Klammern. Dieser Prozess wird auch **Aggregation** genannt, was es uns ermöglicht, Ergebnisse zu kombinieren, indem wir Datensätze auf der Basis von Werten gruppieren und Berechungen innerhalb der Gruppe anwenden.

Im Moment ist es noch schwierig zu sagen, welche ISSN die höchste durchschnittliche Zitationszahl und welche die geringste hat. Wir können die obige Abfrage verbessern, indem wir `ORDER BY` und `DESC` verwenden. 

~~~
SELECT ISSNs, AVG(Citation_Count)
FROM articles
GROUP BY ISSNs 
ORDER BY AVG(Citation_Count) DESC;
~~~

> ## Herausforderung
> Schreibe eine Abfrage mit einer Aggregation, die die Anzahl  der `Title` pro `ISSN` zurückgibt. 
> Die Ausgabe soll dabei die Anzahl der `Title` in absteigender Reihenfolge anzeigen. 
> Mögliche Aggregatfunktionen: `MAX, MIN, AVG, COUNT, SUM`
>
> > ## Lösung
> > ~~~
> > SELECT ISSNs, COUNT(Title)
> > FROM articles
> > GROUP BY ISSNs
> > ORDER BY Citation_Count DESC;
> > ~~~


## Das Schlüsselwort `HAVING`

SQL bietet einen Mechanismus zum Filtern der Ergebnisse auf der Grundlage von Aggregatfunktionen durch das Schlüsselwort `HAVING`.

**Anmerkung**: Der Unterschied zwischen where- und have-Klausel in SQL besteht darin, 
dass where zum Filtern von Datensätzen verwendet wird, bevor eine 
Gruppierung oder Aggregation erfolgt, während have zum Filtern von 
Datensätzen nach einer Gruppierung oder einer Aggregation verwendet wird.

Zum Beispiel können wir die letzte Anfrage, die wir geschrieben haben, so anpassen, dass nur Informationen über die Zeitschrift `ISSNs` 
mit 10 oder mehr veröffentlichten Artikeln zurückgegeben werden:

~~~
SELECT ISSNs, COUNT(*)
FROM articles
GROUP BY ISSNs
HAVING COUNT(Title) >= 10;
~~~

Das Schlüsselwort `HAVING` funktioniert genau wie das Schlüsselwort `WHERE`, verwendet aber Aggregatfunktionen anstelle von Datenbankfeldern.  Wenn Sie auf der Basis einer Aggregation wie `MAX, MIN, AVG, COUNT, SUM` filtern wollen, verwenden Sie `HAVING`; um auf der Basis der einzelnen Werte in einem Datenbankfeld zu filtern, verwenden Sie `WHERE`.

Beachten Sie, dass `HAVING` _nach_ `GROUP BY` kommt. Eine Möglichkeit, darüber nachzudenken, ist: Die Daten werden abgerufen (`SELECT`), können gefiltert werden (`WOERE`), dann in Gruppen zusammengefasst werden (`GROUP BY`); schließlich wählen wir nur einige dieser Gruppen aus (`HAVING`).

> ## Herausforderung
> Schreiben Sie eine Abfrage, die aus der Tabelle `Artikel` die durchschnittliche `Zitieranzahl` für jede Zeitschriften-ISSN zurückgibt 
> aber nur für die Zeitschriften mit durchschnittlich 5 oder mehr Zitaten.
>
> > ## Lösung
> > ~~~
> > SELECT ISSNs, AVG(Citation_Count)
> > FROM articles
> > GROUP BY ISSNs
> > HAVING AVG(Citation_Count)>=5;
> > ~~~

## Berechnungen

In SQL können wir auch Berechnungen durchführen, während wir die Datenbank abfragen. Auch als berechnete Spalten bekannt, können wir Ausdrücke auf einer Spalte oder mehreren Spalten verwenden, um während unserer Abfrage neue Werte zu erhalten. Was wäre zum Beispiel, wenn wir eine neue Spalte namens `CoAuthor_Count` berechnen wollten:

~~~
SELECT Title, ISSNs, Author_Count -1
FROM articles
ORDER BY Author_Count -1 DESC;
~~~

Wir können beliebige arithmetische Operatoren (`+`, `-`, `*`, und `/`) verwenden, wenn wir das möchten.

Wenn Sie mehr über berechnete Werte erfahren möchten, enthält die Lektion zu Software Carpentry Databases and SQL eine nützliche Episode über [Calculating New Values] (https://swcarpentry.github.io/sql-novice-survey/04-calc/index.html). 
