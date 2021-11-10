---
Titel: "Filtern
Lehre: 20
Übungen: 10
Fragen:
- "Wie kann ich Daten filtern?"
Ziele:
- "Abfragen schreiben, die Daten auf der Grundlage von Bedingungen `Auswählen`, wie z.B. `Ende`, `Oder` und `Nicht`.
- "Verstehen, wie man die `WO`-Klausel in einer Aussage verwendet."
- "Lernen, wie man Vergleichsschlüsselwörter wie `LIKE` in einer Aussage verwendet."
Schlüsselpunkte:
- "Verwenden Sie `WO`, um Daten auf der Grundlage bestimmter Bedingungen zu filtern und abzurufen.
- "Verwenden Sie `AND, OR, and NOT`, um zusätzliche Bedingungen hinzuzufügen.
- "Verwenden Sie das Vergleichsschlüsselwort `LIKE` und Platzhalterzeichen wie `%`, um Muster abzugleichen.
---


## Filterung

SQL ist ein leistungsfähiges Werkzeug zum Filtern von Daten in Datenbanken auf der Grundlage einer Reihe von Bedingungen. Nehmen wir an, wir wollen nur Daten für eine bestimmte ISSN, zum Beispiel für die Zeitschrift _Acta Crystallographica_ aus der Tabelle `Artikel`. Die Zeitschrift hat den ISSN-Code `2056-9890`.  Um nach diesem ISSN-Code zu filtern, werden wir die `WOERE`-Klausel verwenden.

~~~
SELECT *
FROM articles
WHERE ISSNs='2056-9890';
~~~
{: .sql}


Wir können zusätzliche Bedingungen hinzufügen, indem wir `AND`, `OR`, und/oder `NOT` verwenden. Nehmen wir zum Beispiel an, wir möchten, dass die Daten über _Acta Crystallographica_ nach Oktober veröffentlicht werden:

~~~
SELECT *
FROM articles
WHERE (ISSNs='2056-9890') AND (Month > 10);
~~~
{: .sql}

Klammern dienen in diesem Fall lediglich der Lesbarkeit, können aber vom SQL-Interpreter zur Eindeutigkeit von Formeln benötigt werden.

Wenn wir Daten für die Zeitschriften *Humanities* und *Religions* erhalten wollen, die
ISSNs Codes "2076-0787" und "2077-1444", können wir die Tests mit OR kombinieren:

~~~
SELECT *
FROM articles
WHERE (ISSNs = '2076-0787') OR (ISSNs = '2077-1444');
~~~
{: .sql}

Wenn Sie nicht den gesamten Wert kennen, nach dem Sie suchen, können Sie Vergleichsschlüsselwörter wie `LIKE`, `IN`, `BETWEEN...AND`, `IS NULL` verwenden. Zum Beispiel können wir `LIKE` in Kombination mit `WOERE` verwenden, um nach Daten zu suchen, die einem Muster entsprechen.

Wenn wir z.B. die Tabelle `Artikel` erneut verwenden, wählen wir alle Daten aus, `WO` das `Subjekt` "Kristallstruktur" enthält:

~~~
SELECT *
FROM articles
Where Subjects LIKE '%Crystal Structure%';
~~~
{: .sql}

Vielleicht ist Ihnen das Platzhalterzeichen `%` aufgefallen. Es wird verwendet, um Null mit vielen Zeichen abzugleichen. In der obigen SQL-Anweisung stimmt es also mit null oder mehr Zeichen vor und nach 'Crystal Structure' überein. 

Lassen Sie uns sehen, welche Variationen des Begriffs wir haben. Beachten Sie Groß- und Kleinschreibung, die Hinzufügung von 's' am Ende von Strukturen usw.

Um mehr über andere Vergleichsschlüsselwörter zu erfahren, die Sie verwenden können, lesen Sie Anfänger-SQL-Lernprogramm auf [SQL-Vergleichsschlüsselwörter](https://beginner-sql-tutorial.com/sql-like-in-operators.htm).


> ## Herausforderung
> Schreiben Sie eine Abfrage, die den `Title`, `First_Author`, `Subjects`, `ISSNs`, `Month` und `Year` zurückgibt
> für alle Arbeiten, bei denen `Subjects` "computer" enthält und die mehr als 4 Zitate haben.
>
> > ## Lösung
> > ~~~
> > SELECT Title, FIRST_Author, Subjects, ISSNs, Month, Year
> > FROM articles
> > WHERE (Subjects LIKE '%computer%') UND (Citation_Count > 4);
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

Sie können weiterhin Bedingungen hinzufügen oder verketten und fortgeschrittenere Abfragen schreiben.
