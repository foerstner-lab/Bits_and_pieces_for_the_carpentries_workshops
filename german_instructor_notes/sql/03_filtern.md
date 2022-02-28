---
Titel: "Filtern
Lehre: 20
Übungen: 10
Fragen:
- "Wie kann ich Daten filtern?"
Ziele:
- "Abfragen schreiben, die Daten auf der Grundlage von Bedingungen `SELECT`, wie z.B. `AND`, `OR` und `NOT`.
- "Verstehen, wie man die `WHERE`-Klausel in einer Aussage verwendet."
- "Lernen, wie man Vergleichsschlüsselwörter wie `LIKE` in einer Aussage verwendet."
Schlüsselpunkte:
- "Verwende `WHERE`, um Daten auf der Grundlage bestimmter Bedingungen zu filtern und abzurufen.
- "Verwende `AND, OR, and NOT`, um zusätzliche Bedingungen hinzuzufügen.
- "Verwende das Keyword `LIKE` und Platzhalterzeichen wie `%`, um Muster abzugleichen.
---

## Filtern

Mit SQL können wir Daten in Datenbanken nach Bedingungen filtern. Nehmen wir an, wir wollen nur Daten für eine bestimmte ISSN, zum Beispiel für die Zeitschrift _Acta Crystallographica_ aus der Tabelle `articles`. Die Zeitschrift hat den ISSN-Code `2056-9890`.  Um nach dieser ISSN zu filtern, werden wir das Keyword `WHERE` verwenden.

~~~
SELECT *
FROM articles
WHERE ISSNs='2056-9890';
~~~

Wir können zusätzliche Bedingungen hinzufügen, indem wir `AND`, `OR`, und/oder `NOT` verwenden. Nehmen wir zum Beispiel an, wir möchten, dass die Daten über _Acta Crystallographica_ nach Oktober veröffentlicht werden:

~~~
SELECT *
FROM articles
WHERE (ISSNs='2056-9890') AND (Month > 10);
~~~

Klammern dienen in diesem Fall lediglich der Lesbarkeit, können aber vom SQL-Interpreter zur Eindeutigkeit von Formeln benötigt werden.

Wenn wir Daten für die ISSNs "2076-0787" und "2077-1444" wollen, können wir diese mit OR kombinieren:

~~~
SELECT *
FROM articles
WHERE (ISSNs = '2076-0787') OR (ISSNs = '2077-1444');
~~~

Wenn Sie nicht den gesamten Wert kennen, nach dem Sie suchen, können Sie Vergleichs-Keywords wie `LIKE`, `IN`, `BETWEEN...AND`, `IS NULL` verwenden. Zum Beispiel können wir `LIKE` in Kombination mit `WHERE` verwenden, um nach Daten zu suchen, die einem Muster entsprechen.

Wenn wir die Tabelle `articles` erneut verwenden, wählen wir alle Daten aus, `WO` die Spalte `Subjects` "crystal structure" enthält:

~~~
SELECT *
FROM articles
Where Subjects LIKE '%crystal structure%';
~~~

Wir verwenden das Platzhalterzeichen `%`, um anzugeben, dass ein oder mehrere Zeichen vor und nach `crystal structure` stehen dürfen.
Die Abfrage `'%crystal structure%'` ist nicht case-sensitiv.

Wir werden uns nicht mehr `BETWEEN...AND`, `IS NULL` anschauen. Hier findet ihr mehr zu diesen Keywords: [SQL-Vergleichs-Keywords](https://beginner-sql-tutorial.com/sql-like-in-operators.htm).


> ## Herausforderung
> Schreibt eine Abfrage, die den `Title`, `First_Author`, `Subjects`, `ISSNs`, `Month` und `Year` zurückgibt.
> Die Ausgabe soll nur Treffer enthalten die das Wort `computer` in der Spalte `Subjects` enthalten und mehr als 4 Zitate haben (`Citation_Count` Spalte).
>
> > ## Lösung
> > ~~~
> > SELECT Title, First_Author, Subjects, ISSNs, Month, Year
> > FROM articles
> > WHERE (Subjects LIKE '%computer%') AND (Citation_Count > 4);
> > ~~~
