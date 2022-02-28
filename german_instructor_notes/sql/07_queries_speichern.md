---
Titel: "Queries speichern"
Lehre: 20
Übungen: 10
Fragen:
- "Wie kann ich eine Anfrage für die zukünftige Verwendung speichern?
- "Wie kann ich eine gespeicherte Abfrage entfernen?
Ziele:
- "Lernen, wie man wiederholte Abfragen als 'Ansichten' speichert und wie man sie fallen lässt."
Schlüsselpunkte:
- "Durch das Speichern von Abfragen als 'Ansichten' können wir Zeit sparen und vermeiden, denselben Vorgang mehrmals zu wiederholen.
---

## Speichern von Abfragen zur zukünftigen Verwendung

Es ist nicht ungewöhnlich, dieselbe Operation mehr als einmal zu wiederholen. 
SQL verfügt über einen sehr leistungsfähigen Mechanismus
um dies zu tun: Ansichten. Views sind in der Datenbank gespeicherte Abfragen, die 
wir wiederum als Tabelle abfragen können.

Um einen View aus einer Abfrage zu erstellen, nutzen wir `CREATE VIEW viewname AS`. 
Wenn wir zum Beispiel die Abfrage speichern wollen, indem wir
die Anzahl der Title in einer Ansicht, die wir schreiben können:

~~~
CREATE VIEW journal_counts AS
SELECT ISSNs, COUNT(Title)
FROM articles
GROUP BY ISSNs;
~~~

Jetzt können wir auf diese Ergebnisse mit einer viel kürzeren Notation zugreifen:

~~~
SELECT *
FROM journal_counts;
~~~

Angenommen, wir brauchen diese Ansicht nicht mehr, können wir sie aus der Datenbank entfernen:

~~~
DROP VIEW journal_counts;
~~~

In DBBrowser for SQLite können auch eine Ansicht von jeder Abfrage erstellen, indem wir auf das kleine Speicher 
Symbol unten auf der Registerkarte SQL ausführen und klicken Sie dann auf __Speichern unter Ansicht__. 


> ## Herausforderung
>
> Schreibe eine `CREATE VIEW`-Abfrage, die die Tabelle `articles` mit der 
> `journals"-Tabelle über `ISSNs` und gebe die Anzahl der 'Titles' zurück 
> gruppiert nach dem `Journal_Title` in der Reihenfolge absteigend. 
>
> > ## Lösung
> > ~~~
> > CREATE VIEW journal_counts AS
> > SELECT journals.Journal_Title, COUNT(Title)
> > FROM articles
> > JOIN journals
> > ON articles.ISSNs = journals.ISSNs
> > GROUP BY Journal_Title
> > ORDER BY COUNT(Title) DESC
> > ~~~
>
