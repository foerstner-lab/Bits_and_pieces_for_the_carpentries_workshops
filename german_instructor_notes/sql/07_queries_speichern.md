---
Titel: "Anfragen speichern
Lehre: 20
Übungen: 10
Fragen:
- "Wie kann ich eine Anfrage für die zukünftige Verwendung speichern?
- "Wie kann ich eine gespeicherte Abfrage entfernen?
Ziele:
- "Lernen Sie, wie man wiederholte Abfragen als 'Ansichten' speichert und wie man sie fallen lässt."
Schlüsselpunkte:
- "Durch das Speichern von Abfragen als 'Ansichten' können Sie Zeit sparen und vermeiden, denselben Vorgang mehrmals zu wiederholen.
---

## Speichern von Abfragen zur zukünftigen Verwendung

Es ist nicht ungewöhnlich, dieselbe Operation mehr als einmal zu wiederholen, zum Beispiel
für Überwachungs- oder Berichtszwecke. SQL verfügt über einen sehr leistungsfähigen Mechanismus
um dies zu tun: Ansichten. Views sind in der Datenbank gespeicherte Abfragen. Sie fragen sie als 
(virtuelle) Tabelle, die jedes Mal, wenn Sie sie abfragen, aufgefüllt wird.

Um einen View aus einer Abfrage zu erstellen, müssen Sie `CREATE VIEW viewname AS` hinzufügen.
vor der eigentlichen Abfrage. Wenn wir zum Beispiel die Abfrage speichern wollen, indem wir
die Anzahl der Zeitschriften in einer Ansicht, die wir schreiben können:

~~~
CREATE VIEW journal_counts AS
SELECT ISSNs, COUNT(*)
FROM articles
GROUP BY ISSNs;
~~~
{: .sql}

Jetzt können wir auf diese Ergebnisse mit einer viel kürzeren Notation zugreifen:

~~~
SELECT *
FROM journal_counts;
~~~
{: .sql}

Angenommen, wir brauchen diese Ansicht nicht mehr, können wir sie aus der Datenbank entfernen.
fast so, als ob wir einen Tisch hätten:

~~~
DROP VIEW journal_counts;
~~~
{: .sql}

In DBBrowser for SQLite können Sie auch eine Ansicht von jeder Abfrage erstellen, indem Sie Folgendes weglassen 
die Anweisung `CREATE VIEW viewname AS` und klicken Sie stattdessen auf die kleine Save 
Symbol unten auf der Registerkarte SQL ausführen und klicken Sie dann auf __Speichern unter Ansicht__. 
Unabhängig von der Methode, die Sie zum Erstellen einer Ansicht verwenden, wird diese in der Liste der Ansichten angezeigt 
unter dem Register Datenbankstruktur.


> ## Herausforderung
>
> Schreibe eine `CREATE VIEW`-Abfrage, die die Tabelle `articles` mit der 
> `journals"-Tabelle über `ISSNs` und gebe die Anzahl der Artikel zurück 
> gruppiert nach dem `Journal_Title` in der Reihenfolge absteigend. 
>
> > ## Lösung
> > ~~~
> > CREATE VIEW journal_counts AS
> > SELECT journals.Journal_Title, COUNT(*)
> > FROM articles
> > JOIN journals
> > ON articles.ISSNs = journals.ISSNs
> > GROUP BY Journal_Title
> > ORDER BY COUNT(*) DESC
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}
