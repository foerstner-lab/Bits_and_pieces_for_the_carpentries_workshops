# SQL Übungen aus der Lesson

## 1. Übung - Auswählen und Sortieren von Daten (Episode 2)

Schreibe eine Abfrage, die `Title`, `First_Author`, `ISSNs` und `Citation Count` aus 
der Tabelle `articles` zurückgibt. Ordne die Ausgabe nach dem höchsten `Citation_Count` und alphabetisch nach `Title`.

```
SELECT Titel, Erster_Autor, ISSNs, Citation_Count
FROM-Artikel
ORDER BY Citation_Count DESC, Titel ASC;
```

## 2. Übung - Filtern (Episode 3)

Schreibe eine Abfrage, die den `Title`, `First_Author`, `Subjects`, `ISSNs`, `Month` und `Year` zurückgibt. 
Die Ausgabe soll nur Treffer enthalten die das Wort "computer" in der Spalte `Subjects` enthalten 
und mehr als 4 Zitate haben (`Citation_Count` Spalte).

```
SELECT Title, First_Author, Subjects, ISSNs, Month, Year
FROM articles
WHERE (Subjects LIKE '%computer%') AND (Citation_Count > 4);
```
## 3. Übung - Aggregationen (Episode 5)

Schreibe eine Abfrage mit einer Aggregatfunktion, die die Anzahl 
der Artikeltitel pro ISSN, sortiert nach Titelanzahl in absteigender 
Reihenfolge, zurückgibt. Welche ISSN hat die meisten Titel? 
(MAX, MIN, AVG, COUNT, SUM)
```
SELECT ISSNs, COUNT(Title)
FROM articles
GROUP BY ISSNs
ORDER BY Title DESC;
```
**Anmerkung**: Der Unterschied zwischen where- und have-Klausel in SQL besteht darin, 
dass where zum Filtern von Datensätzen verwendet wird, bevor eine 
Gruppierung oder Aggregation erfolgt, während have zum Filtern von 
Datensätzen nach einer Gruppierung oder einer Aggregation verwendet wird.

## 4. Übung - Having (Episode 5)

Schreibe eine Abfrage, die aus der Tabelle articles die 
durchschnittliche Zitationsanzahl für jede Zeitschriften-ISSN 
zurückgibt aber nur für die Zeitschriften mit durchschnittlich 
5 oder mehr Zitaten.
```
SELECT ISSNs, AVG(Citation_Count)
FROM articles
GROUP BY ISSNs
HAVING AVG(Citation_Count)>=5;
```
## 5. Übung  - Join (Episode 6)

Schreibe eine Abfrage, die die Tabellen articles und journals verbindet 
und die den Journal_Title, die Gesamtzahl der veröffentlichten Artikel 
und die durchschnittliche Anzahl der Zitationen für jede ISSN 
zurückgibt.
```
SELECT journals.Journal_Title, count(*), avg(articles.Citation_Count)
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs
GROUP BY articles.ISSNs;
```
## 6. Übung - Join (Episode 6)

Schreibe eine Abfrage, die den Journal_Title, den Publisher und 
die Anzahl der veröffentlichten Artikel, geordnet nach der Anzahl der 
Artikel in absteigender Reihenfolge ausgibt.
```
SELECT journals.Journal_Title, publishers.Publisher, COUNT(*)
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs
JOIN publishers
ON publishers.id = journals.PublisherId
GROUP BY Journal_Title
ORDER BY COUNT(*) DESC;
```
## 7. Übung - Create View (Episode 7)

Schreibe eine CREATE VIEW Abfrage, die die Tabelle articles mit der journals Tabelle 
über ISSNs verknüpft und die Zahl der Artikel zurückgibt, gruppiert nach dem Journal_Title in absteigender Reihenfolge
```
CREATE VIEW journal_counts AS
SELECT journals.Journal_Title, COUNT(*)
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs
GROUP BY Journal_Title
ORDER BY COUNT(*) DESC
```
### Gruppenaufgaben (Episode 08)

**Anmerkung**: Die Teilnehmer:innen in 3-4 Gruppen in Breakout-Rooms zur Bearbeitung dieser Übungen schicken. Bearbeitungszeit sind ca. 45 Minuten.

1. Wie viele Artikel gibt es von jedem Erstautor? Vergebe einen Alias für die Anzahl der Artikel und ordne die Ergebnisse nach Artikeln
```
SELECT First_Author, COUNT( * ) AS n_articles
FROM articles
GROUP BY First_Author
ORDER BY n_articles DESC;
```
2. Wie viele Arbeiten hat ein einzelner Autor? Wie viele haben 2 Autoren? Wieviele 3? etc?
```
SELECT Author_Count, COUNT( * )
FROM articles
GROUP BY Author_Count;
```
3. Wie viele Artikel werden für jede Sprache veröffentlicht? Ignoriere die Artikel, bei denen die Sprache unbekannt ist.
```
SELECT Language, COUNT( * )
FROM articles
JOIN languages
ON articles.LanguageId=languages.id
WHERE Language != ''
GROUP BY Language;
```
4. Wie viele Artikel werden für jeden Lizenztyp veröffentlicht, und was ist die Durchschnittsanzahl der Zitationen für den jeweiligen Lizenztyp?
```
SELECT Licence, AVG( Citation_Count ), COUNT( * )
FROM articles
JOIN licences
ON articles.LicenceId=licences.id
GROUP BY Licence;
```
5. Schreibe eine Abfrage die Titel, Erstautor, Autorenzahl, Zitierzahl, Monat, Jahr, Zeitschriftentitel und Herausgeber für Artikel in der Datenbank zurückgibt.
```
SELECT Title, First_Author, Author_Count, Citation_Count, Month, Year, Journal_Title, Publisher
FROM articles
JOIN journals
ON articles.issns=journals.ISSNs
JOIN publishers
ON publishers.id=journals.PublisherId;
```

## Episode 10 Gruppenaufgaben - Aufgabenstellung Zum Kopieren in das Pad

1. Wie viele Artikel gibt es von jedem Erstautor? Vergebe einen Alias für die Anzahl der Artikel und ordne die Ergebnisse nach Artikeln

2. Wie viele Arbeiten hat ein einzelner Autor? Wie viele haben 2 Autoren? Wieviele 3? etc?

3. Wie viele Artikel werden für jede Sprache veröffentlicht? Ignoriere die Artikel, bei denen die Sprache unbekannt ist.

4. Wie viele Artikel werden für jeden Lizenztyp veröffentlicht, und was ist die Durchschnittsanzahl der Zitationen für den jeweiligen Lizenztyp?

5. Schreibe eine Abfrage die Titel, Erstautor, Autorenzahl, Zitierzahl, Monat, Jahr, Zeitschriftentitel und Herausgeber für Artikel in der Datenbank zurückgibt.
