---
Titel: "Joins und Aliasse"
Lehre: 25
Übungen: 20
Fragen:
- "Wie schließe ich zwei Tische zusammen, wenn sie einen gemeinsamen Informationspunkt haben?
- "Wie kann ich Aliase verwenden, um meine Abfragen zu verbessern?
Ziele:
- "Verstehen, wie man Tabellen über Joins miteinander verknüpft.
- "Verstehen, wann es sinnvoll ist, Aliase oder Stenogramme zu verwenden.
Schlüsselpunkte:
- "Das Verbinden zweier Tabellen in SQL ist eine gute Möglichkeit, Datensätze zu analysieren, insbesondere wenn beide Datensätze Teilantworten auf die Fragen geben, die Sie stellen möchten.
- Die Erstellung von Aliasen ermöglicht es uns, weniger Zeit mit dem Eintippen und mehr Zeit mit Abfragen zu verbringen!
---

## Joins

Die SQL-Klausel `JOIN` erlaubt es uns, Spalten aus einer oder mehreren Tabellen in einer Datenbank zu kombinieren, indem wir Werte verwenden, die allen gemeinsam sind. Sie folgt der "FROM"-Klausel in einer SQL-Anweisung. Wir müssen dem Computer auch mitteilen, welche Spalten die Verbindung zwischen den beiden
Tabellen mit dem Wort `ON`.  

Beginnen wir damit, die Daten aus der "Artikel"-Tabelle mit der "Zeitschriften"-Tabelle zu verbinden. Die `ISSNs`-Spalten in diesen beiden Tabellen verbinden sie.

~~~
SELECT *
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs;
~~~
{: .sql}

`On` ist ähnlich wie `WHERE`, es filtert Dinge nach einer Testbedingung heraus.  Wir benutzen das Format `table.colname`, um dem SQL-Manager mitzuteilen, auf welche Spalte in welcher Tabelle wir uns beziehen.

Alternativ können wir das Wort `USING` als Kurzform verwenden.  In diesem Fall teilen wir DB Browser mit, dass wir `Artikel` mit `Journalen` kombinieren wollen und dass die gemeinsame Spalte `ISSNs` ist.

~~~
SELECT *
FROM articles
JOIN journals
USING (ISSNs);
~~~
{: .sql}

Diese Abbildung zeigt die Beziehungen zwischen den Tabellen und hilft bei der Visualisierung des Zusammenfügens oder Verknüpfens der Tabellen in der Datenbank:
![Artikeldatenbank](../Assets/img/Artikel-erd-v02.png)
Über [relationales Datenbankdesign] (https://librarycarpentry.org/lc-sql/08-database-design/index.html) werden wir in der nächsten Episode berichten. Zusätzlich zu den obigen visuellen Erläuterungen bietet *[SQL Join Types Explained Visually](https://dataschool.com/how-to-teach-people-sql/sql-join-types-explained-visually/)* visuelle/animierte Beispiele, die den Lernenden helfen sollen, zu vermitteln, was in SQL `JOIN`s geschieht.

Wenn Sie Tabellen verbinden, können Sie die gewünschten Spalten mit `table.colname` angeben, anstatt alle Spalten mit `*` auszuwählen. Zum Beispiel:

~~~
SELECT articles.ISSNs, journals.Journal_Title, articles.Title, articles.First_Author
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs;
~~~
{: .sql}

Verknüpfungen können mit Sortieren, Filtern und Aggregation kombiniert werden.  Wenn wir also die durchschnittliche Anzahl der Autoren für Artikel in jeder Zeitschrift ermitteln wollten, können wir die folgende Abfrage verwenden:

~~~
SELECT articles.ISSNs, journals.Journal_Title, ROUND(AVG(articles.Author_Count), 2)
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs
GROUP BY articles.ISSNs;
~~~
{: .sql}

Die Funktion `ROUND` erlaubt es uns, die von der Funktion `AVG` zurückgegebene `Author_Count`-Zahl um 2 Dezimalstellen zu runden.

> ## Herausforderung
> Schreiben Sie eine Abfrage, die die Tabellen `Artikel` und `Journale` verbindet und die den `Journal_Title`, die Gesamtzahl der veröffentlichten Artikel und die durchschnittliche Anzahl der Zitate für jede Zeitschriften-ISSN zurückgibt.
>
> > ## Lösung
> > ~~~
> > SELECT journals.Journal_Title, COUNT(*), AVG(articles.Citation_Count)
> > FROM articles
> > JOIN journals
> > ON articles.ISSNs = journals.ISSNs
> > GROUP BY articles.ISSNs;
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

Sie können auch mehrere Tabellen verbinden. Zum Beispiel:

~~~
SELECT articles.Title, articles.First_Author, journals.Journal_Title, publishers.Publisher
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs
JOIN publishers
ON publishers.id = journals.PublisherId;
~~~
{: .sql}

> ## Herausforderung:
>
> Schreiben Sie eine Abfrage, die den `Journal_Titel`, den `Verlagsnamen` und die Nummer von
> veröffentlichte Artikel, geordnet nach der Anzahl der Artikel in absteigender Reihenfolge.
>
> > ## Lösung
> > ~~~
> > SELECT journals.Journal_Title, publishers.Publisher, COUNT(*)
> > FROM articles
> > JOIN journals
> > ON articles.ISSNs = journals.ISSNs
> > JOIN publishers
> > ON publishers.id = journals.PublisherId
> > GROUP BY Journal_Title
> > ORDER BY COUNT(*) DESC;
> > ~~~
> > {: .sql}
> {: .lösung}
{: .herausfordern}

Es gibt verschiedene Arten von Joins, über die Sie unter [SQL Joins Explained](http://www.sql-join.com/sql-join-types) mehr erfahren können.


## Aliasnamen

Da die Anfragen immer komplexer werden, können die Namen lang und unhandlich werden. Um die Dinge klarer zu machen, können wir Aliase verwenden, um den Elementen in der Abfrage neue Namen zuzuweisen.

Wir können beide Tabellennamen aliasisieren:

~~~
SELECT ar.Title, ar.First_Author, jo.Journal_Title
FROM articles AS ar
JOIN journals AS jo
ON ar.ISSNs = jo.ISSNs;
~~~
{: .sql}

Und Spaltennamen:

~~~
SELECT ar.title AS title, ar.first_author AS author, jo.journal_title AS journal
FROM articles AS ar
JOIN journals  AS jo
ON ar.issns = jo.issns;
~~~
{: .sql}

Das `AS` ist technisch nicht erforderlich, Sie könnten es also tun:

~~~
SELECT a.Title t
FROM articles a;
~~~
{: .sql}

Aber die Verwendung von `AS` ist viel klarer, so dass es ein guter Stil ist, es einzubeziehen.
