---
Titel: "Datenbank-Design
Lehre: 25
Übungen: 20
Fragen:
- "Was ist Datenbankdesign?"
Ziele:
- "Verwendung von Entity-Relationship-Diagrammen zur Visualisierung und Strukturierung Ihrer Daten".
Schlüsselpunkte:
- "Datenbank-Design ist hilfreich für die Erstellung effizienterer Datenbanken."
---

## Tabellenkalkulationen

In Bibliotheken werden häufig Tabellenkalkulationen erstellt, um Listen mit einer Vielzahl von Dingen zu führen, von der Inventarisierung von Objekten bis hin zur Überprüfung und Auswahl von Ressourcen (siehe _[Welche Verwendungsmöglichkeiten gibt es für SQL in Bibliotheken?](https://librarycarpentry.org/lc-sql/01-introduction/index.html)_. Tabellenkalkulationen, auch bekannt als tabellarische Daten oder flache Dateien, sind eine einfache Möglichkeit, Daten nach Spalten und Zeilen geordnet aufzulisten. Spaltenüberschriften beschreiben die in den entsprechenden Spalten enthaltenen Daten. Jede Zeile ist ein Datensatz mit Daten über sie, die in separaten Spaltenzellen enthalten sind.

Tabellenkalkulationen können die Datenerfassung erleichtern, aber sie können auch zu unordentlichen Daten führen.

>## Identifizieren von Inkonsistenzen in Tabellenkalkulationsdaten
>
> Können Sie in der Abbildung unten erkennen, wo Inkonsistenzen in den Daten eingeführt wurden?
>
> ![OpenRefine DOAJ Sample Article Data](../assets/img/doaj-spreadsheet.png)
>
> > ## Antworten
> > 1. Die Daten in der Spalte "Sprache" sind auf zwei Arten formatiert, als Abkürzung und als ganzes Wort;
> > 2. Die vollen Namen der Autoren werden verwendet, in der Reihenfolge Vorname bis Nachname, wobei der Mittelname abgekürzt und durch Pipes getrennt wird;
> > 3. Das Datumsformat ist MM/DD/YYYYY und nicht das üblicherweise verwendete ISO 8601-Format; 
> > 4. Die Spalte "Subjects" grenzt Daten durch Pipes ab, und die Daten liegen in einer Vielzahl von Formaten wie Abkürzungen, Klassifikationen und manchmal in Großbuchstaben vor. 
> > **Kannst du noch etwas anderes erkennen?**
> {: .lösung}
{: .herausfordern}

Wenn Sie mit der Zeit genügend Daten in Tabellenkalkulationen sammeln, werden Sie wahrscheinlich im Laufe der Zeit inkonsistente Daten erhalten (d.h. falsch formatierte, falsch geschriebene Daten). Datenbankdesign kann dabei helfen.

## Datenbank-Design

Das Datenbankdesign beinhaltet ein Modell oder einen Plan, das/der entwickelt wurde, um zu zeigen, wie die Daten gespeichert, organisiert und manipuliert werden können. Der Entwurf befasst sich mit der Frage, welche Daten gespeichert werden müssen, wie sie klassifiziert werden könnten und er identifiziert die Beziehungen zwischen den Daten.

## Terminologie
<img src="../assets/img/field-record-value.png" alt="Felder, Datensätze, Werte" width="500"/>

In der Lektion [Einführung in SQL] (https://librarycarpentry.org/lc-sql/01-introduction/index.html) haben wir die Begriffe "Felder", "Datensätze" und "Werte" eingeführt. Diese Begriffe werden häufig in Datenbanken verwendet, während die Begriffe "Spalten", "Zeilen" und "Zellen" in Tabellenkalkulationen gebräuchlicher sind. Felder speichern eine einzige Art von Informationen (Text, ganze Zahlen usw.), Datensätze sind eine Reihe von Feldern, die bestimmte Werte enthalten.

Um eine Datenbank zu entwerfen, müssen wir zunächst entscheiden, welche Art von Dingen wir als Tabellen darstellen wollen. Eine Tabelle ist die physische Manifestation einer "Entität". Eine Entität ist die konzeptionelle Darstellung des Dings, das wir in der Datenbank speichern wollen. Eine Entität hat "Attribute", die sie beschreiben. Zum Beispiel ist ein Artikel oder eine Zeitschrift eine Entität. Attribute sind z.B. der Titel des Artikels oder die ISSN der Zeitschrift.  

Um eine Datenbank zu entwerfen, ist es nützlich, auf einer abstrakten Ebene die Entitäten zu beschreiben, die wir erfassen möchten, und zu beschreiben, wie die verschiedenen Entitäten miteinander in Beziehung stehen. Wir tun dies mit Hilfe eines Entitätsbeziehungsdiagramms (ER-Diagramm oder ERD).

## Entitäts-Beziehungsdiagramm (ER-Diagramm oder ERD)

ERDs sind hilfreiche Werkzeuge, um Ihre Daten effizienter zu visualisieren und zu strukturieren. Sie ermöglichen es Ihnen, Beziehungen zwischen Konzepten abzubilden und letztendlich eine relationale Datenbank zu erstellen. Im Folgenden finden Sie einen ERD der in dieser Lektion verwendeten Datenbank:

![Artikel-Datenbank](../Assets/img/Artikel-erd.png)
*Oder Sie können die [dbdiagram.io interaktive Version des ERD](https://dbdiagram.io/d/5cc32b0cf7c5bb70c72fc530)* ansehen.

Die Beziehungen zwischen Entitäten und ihren Attributen werden durch Linien dargestellt, die sie miteinander verbinden. Beispielsweise wird die Linie, die Zeitschriften und Verlage miteinander verbindet, wie folgt interpretiert: Die Entität "journals" ist mit der Entität "publishers" durch die Attribute "PublisherId" bzw. "id" verbunden.

Konzeptionell wissen wir, dass eine Zeitschrift nur einen Verlag hat, aber ein Verlag kann viele Zeitschriften veröffentlichen. Dies wird als Eins-zu-viele-Beziehung bezeichnet. Bei der Modellierung von Beziehungen weisen wir normalerweise der "einen" Seite der Beziehung einen eindeutigen Identifikator zu und verwenden denselben Identifikator, um auf diese Entität auf der "vielen" Seite zu verweisen. In der "Publisher"-Tabelle ist das "id"-Attribut dieser eindeutige Bezeichner. Wir verwenden denselben Identifikator in der Tabelle "Journals", um auf einen einzelnen Verlag zu verweisen. Auf diese Weise können wir eindeutig unterscheiden, welche Zeitschriften mit welchem Verlag so verbunden sind, dass die Integrität der Daten gewahrt bleibt (siehe Abschnitt "Normalisierung" weiter unten).

## Weitere Terminologie
Am Beispiel des Beispiels Zeitschriften-Verlage wird in der Datenbank das Attribut "id" in "publishers" als Primärschlüssel (PK) und das Attribut "PublisherId" als Fremdschlüssel (FK) bezeichnet. Zusätzlich zu den Eins-zu-viele-Beziehungen (manchmal als 1 zu * oder 1 zu ∞ angegeben, aber es gibt auch andere Schreibweisen), ist eine weitere übliche Beziehung die Eins-zu-viele-Beziehung. Der Grad der Beziehung zwischen Entitäten wird als ihre "Kardinalität" bezeichnet.


## Normalisierung

ERDs sind hilfreich bei der Normalisierung Ihrer Daten, einem Prozess, mit dem Tabellen erstellt und Beziehungen zwischen diesen Tabellen hergestellt werden können, mit dem Ziel, Redundanzen und Inkonsistenzen in den Daten zu beseitigen. 

Im obigen ERD-Beispiel ermöglicht uns die Erstellung einer separaten Tabelle für Verlage und die Verknüpfung mit ihr von der Zeitschriftentabelle aus über PK- und FK-Kennungen die Normalisierung der Daten und die Vermeidung von Inkonsistenzen. Wenn wir eine Tabelle verwenden würden, könnten wir, wie unten gezeigt, Verlagsnamensfehler wie Schreibfehler oder alternative Namen einführen.

Einführen von Inkonsistenzen und Normalisierung der Daten](../assets/img/normalisation.png)

Im Normalisierungsprozess gibt es eine Reihe von normalen Formularen, die Ihnen helfen können, Redundanzen in Datenbanktabellen zu reduzieren. [Study Tonight](https://www.studytonight.com/dbms/database-normalization.php) bietet Tutorials, in denen Sie mehr über diese Formulare erfahren können.  

>## Identifizieren verbleibender Inkonsistenzen in der ERD
>
> Gibt es andere Tabellen und Beziehungen, die Sie erstellen können, um die Daten weiter zu normalisieren und Inkonsistenzen zu vermeiden?
>
> Für diese Übung können Sie entweder Bleistift/Stift und Papier verwenden, um neue Tabellen und Beziehungen zu zeichnen, oder [dbdiagram.io] (https://dbdiagram.io/d/5cc32b0cf7c5bb70c72fc530) verwenden, um die obige ERD zu modifizieren.
>
> > ## Antworten
> > 1. Eine "Autoren"-Tabelle kann mit einer "Many-to-Many"-Beziehung zur "Artikel"-Tabelle und einer [assoziativen Entität] (https://en.wikipedia.org/wiki/Associative_entity) oder einer Brückentabelle zwischen ihnen erstellt werden.
> > 2. Eine "Themen"-Tabelle kann mit einer "Many-to-Many"-Beziehung mit der "Artikel"-Tabelle und einer Brückentabelle zwischen ihnen erstellt werden.
> > >*Kannst du noch etwas anderes erkennen?**
> {: .solution}
{: .challenge}

Zusätzliche Datenbank-Design-Tutorials, die Sie von Lucidchart aus konsultieren können:

* [Tutorial zu Datenbankstruktur und -design](https://www.lucidchart.com/pages/database-diagram/database-design)
* [Was ist ein Entitäts-Beziehungsdiagramm](https://www.lucidchart.com/pages/er-diagrams)
