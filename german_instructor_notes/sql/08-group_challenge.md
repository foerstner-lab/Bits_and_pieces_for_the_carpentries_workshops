---
Titel: "Zusätzliche Herausforderungen (fakultativ)".
Unterricht: 0
Übungen: 35
Fragen:
- "Gibt es zusätzliche Herausforderungen, die Übersetzung von einfachen englischen Abfragen in SQL-Abfragen zu üben?
Ziele:
- "Zusätzliche Herausforderungen, um das Erstellen von SQL-Abfragen zu üben."
Schlüsselpunkte:
- "Es braucht Zeit und Übung, um zu lernen, wie man einfache englische Abfragen in SQL-Abfragen übersetzt.
---

## Zusätzliche Herausforderungen (optional)

SQL-Abfragen helfen uns dabei, *spezifische *Fragen* zu stellen, die wir über unsere Daten beantworten wollen. Die wahre Kunst mit SQL besteht darin, zu wissen, wie man unsere Fragen in eine sinnvolle SQL-Abfrage übersetzt (und anschließend unsere Ergebnisse visualisiert und interpretiert).

Werfen Sie einen Blick auf die folgenden Fragen; diese Fragen sind in einfachem Englisch geschrieben. Können Sie sie in *SQL-Abfragen* übersetzen und eine passende Antwort geben?

Wenn Sie weitere SQL-Konzepte lernen und zusätzliche Herausforderungen ausprobieren möchten, lesen Sie auch die Lektion [Software Carpentry Databases and SQL] (https://swcarpentry.github.io/sql-novice-survey/).

> ## Herausforderung 1
> Wie viele `Artikel` gibt es von jedem `Erstautor`? Können Sie einen Alias für die Anzahl der Artikel vergeben? Können Sie die Ergebnisse nach Artikeln ordnen?
>
> > ## Lösung 1
> > ~~~
> > SELECT Erster_Autor, COUNT( * ) AS n_Artikel
> > FROM-Artikel
> > GRUPPE NACH ERSTER_AUTOR
> > BESTELLUNG DURCH n_Artikel DESC;
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

> ## Herausforderung 2
> Wie viele Arbeiten hat ein einzelner Autor? Wie viele haben 2 Autoren? Wieviele 3? etc?
>
> > ## Lösung 2
> > ~~~
> > SELECT Autor_Zahl, ZAHL( * )
> > FROM-Artikel
> > GRUPPE BY Autor_Anzahl;
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

> ## Herausforderung 3
> Wie viele Artikel werden für jede `Sprache` veröffentlicht? Ignorieren Sie Artikel, bei denen
> Sprache ist unbekannt.
>
> > ## Lösung 3
> > ~~~
> > SELECT Sprache, ZAEHLUNG( * )
> > FROM-Artikel
> > JOIN-Sprachen
> > ON-Artikel.LanguageId=languages.id
> > WHERE Sprache != ''
> > GRUPPE NACH SPRACHE;
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

> ## Herausforderung 4
> Wie viele Artikel werden für jeden `Lizenztyp veröffentlicht, und was ist der Durchschnitt?
> Anzahl der Zitate für diesen `Lizenztyp`?
>
> > ## Lösung 4
> > ~~~
> > SELECT-Lizenz, AVG( Zitat_Zahl ), COUNT( * )
> > FROM-Artikel
> > JOIN-Lizenzen
> > ON-Artikel.lizenzId=lizenzen.id
> > WHERE-Lizenz != ''
> > GRUPPE NACH LIZENZ;
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

> ## Herausforderung 5
> Schreiben Sie eine Abfrage, die `Titel, Erstautor, Autorenzahl, Zitierzahl, Monat, Jahr, Zeitschriftentitel und Herausgeber` für Artikel in der Datenbank zurückgibt.
>
> > ## Lösung 5
> > ~~~
> > SELECT Titel, Erstautor, Autorenzahl, Zitationszahl, Monat, Jahr, Zeitschriftentitel, Herausgeber
> > FROM-Artikel
> > JOIN-Zeitschriften
> > ON articles.issns=Zeitschriften.ISSNs
> > JOIN-Verleger
> > ON publishers.id=Zeitschriften.PublisherId;
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}
