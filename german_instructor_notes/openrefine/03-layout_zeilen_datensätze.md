---
Titel: "Layout von OpenRefine, Rows vs. Records"
Unterricht: 10
Übungen: 5
Fragen:
- "Wie sind die Daten in OpenRefine organisiert?"
- "Wie erhalte ich Zugang zu den Optionen, um Daten in OpenRefine zu ändern?"
- "Was ist der Unterschied zwischen Zeilen und Datensätzen in OpenRefine?"
- Wie kann ich mit einzelnen Zellen arbeiten, die mehrere Werte in einer Liste enthalten?
Ziele:
- Finde die Steuerelemente zum Navigieren in OpenRefine
- Optionen für die Arbeit mit Daten über die OpenRefine-Dropdown-Menüs finden
- Zellen, die mehrere Daten enthalten, so aufteilen, dass jedes Datenelement in einer eigenen Zelle steht
Keypoints:
- "OpenRefine verwendet Zeilen und Spalten, um Daten anzuzeigen"
- Die meisten Optionen für die Arbeit mit Daten in OpenRefine werden über ein Dropdown-Menü am oberen Rand einer Datenspalte aufgerufen.
- Wenn du eine Option in einer bestimmten Spalte auswählst (z.B. um eine Änderung an den Daten vorzunehmen), wirkt sich dies auf alle Zellen in dieser Spalte aus.
- OpenRefine hat einen Datensatzmodus, der mehrere Zeilen zu einem einzigen Datensatz verbindet.
- Mehrwertige Zellen aufteilen und verbinden, um die einzelnen Werte darin zu ändern.
- Wenn du mehrwertige Zellen in deinen Daten erstellst, wähle ein Trennzeichen, das nicht in den Datenwerten vorkommt.
---

## Das Layout von OpenRefine
OpenRefine zeigt die Daten in einem Tabellenformat an. Jede Zeile steht normalerweise für einen "Datensatz" in den Daten, während jede Spalte eine Art von Information darstellt, wie zb in Excel.

OpenRefine zeigt nur eine begrenzte Anzahl von Datenzeilen auf einmal an. Du kannst die Anzahl zwischen 5, 10 (Standard), 25 und 50 oben links in der Datentabelle einstellen. Du kannst durch die Datensätze navigieren, indem du die Navigationsoptionen Vorherige/Nächste/Erste/Letzte oben rechts in der Datentabelle benutzt.

In OpenRefine ist es jederzeit möglich, Änderungen rückgängig zu machen: Beachte das linke Feld, das zurzeit leer ist. Lies die vier Wörter am oberen Rand des Fensters:
Facette/Filter und Rückgängig/Redo.  Wir werden uns später im Workshop mit den Befehlen zum Rückgängigmachen und Wiederherstellen beschäftigen; du kannst sie bei Bedarf jederzeit verwenden. 

## Arbeiten mit Daten in OpenRefine
Die meisten Optionen für die Arbeit mit Daten in OpenRefine werden über Dropdown-Menüs am oberen Rand der Datenspalten aufgerufen. Wenn du eine Option in einer bestimmten Spalte auswählst (z. B. um eine Änderung an den Daten vorzunehmen), wirkt sie sich auf alle Zellen in dieser Spalte aus. Wenn du Änderungen in mehreren Spalten vornehmen willst, musst du dies spaltenweise tun.

## Zeilen und Datensätze
OpenRefine verfügt über zwei Modi zur Anzeige von Daten: "rows" und "records". Im Moment befinden wir uns im Zeilenmodus, in dem jede Zeile einen einzelnen Datensatz darstellt - in diesem Fall einen Artikel. Im Modus "Datensätze" kann OpenRefine mehrere Zeilen miteinander verknüpfen, die zum selben Datensatz gehören. Die Zeilen werden den Datensätzen anhand der Werte in der ersten Spalte zugeordnet. Mehr dazu [Details zu Zeilen und Datensätzen in der OpenRefine-Dokumentation](https://docs.openrefine.org/manual/exploring#rows-vs-records).

### Zellen aufteilen

Um zu sehen, wie das in der Praxis funktioniert, können wir die Autorennamen in separate Zellen aufteilen. Wenn du dir die Autorenspalte ansiehst, solltest du erkennen können, dass sich in jeder Zelle mehrere Namen befinden, die durch das Pipe-Symbol ( \| ) getrennt sind.

Um in OpenRefine effektiv mit den Autorennamen arbeiten zu können, müssen wir jeden Namen in einer eigenen Zelle haben. Um die Namen in ihre eigenen Zellen aufzuteilen, können wir die Funktion "Mehrwertige Zellen aufteilen" verwenden:

* Click the dropdown menu at the top of the Author column
* Choose `Edit cells->Split multi-valued cells`
* In the prompt type the ( \| ) symbol and click `OK`
    * Beachte, dass die Zeilen weiterhin fortlaufend nummeriert sind.
* Click the `Records` option to change to Records mode
    * Beachte, dass sich die Nummerierung geändert hat, was darauf hinweist, dass sich mehrere Zeilen auf denselben Datensatz beziehen.

Beachte in den Bildern oben den Unterschied zwischen: Zeilen mit demselben Titel erscheinen unter jedem gemeinsamen Titel, wobei die nummerierte Reihenfolge in der dritten Spalte von links unterbrochen wird. Gemeinsame Titel haben die gleiche Schattierung, was visuell schwer zu unterscheiden sein kann. Achte daher auf die Sterne und Fähnchen in den Spalten ganz links, die eine neue Zeile, also einen Artikel mit einem anderen Autor, anzeigen.

Jetzt, wo wir mehrwertige Zellen aufteilen können, werden wir uns ansehen, wie wir sie wieder zusammenfügen.

### Zellen zusammenfügen

- Aufteilung der mehrwertigen Zellen in einzelne Zellen (wie oben beschrieben)
- einzelne Zellen ändern/verfeinern/bereinigen
- Mehrwertige Zellen wieder zusammenfügen

Das Ändern von Zellen wird in späteren Lektionen behandelt, aber jetzt wollen wir uns damit beschäftigen, wie man Zellen, die zuvor aufgeteilt wurden, wieder zusammenfügt.

* Klicke auf das Dropdown-Menü oben in der Autorenspalte.
* Wähle "Zellen bearbeiten->Mehrwertige Zellen verbinden".
* Gib in der Eingabeaufforderung das Symbol ( \| ) ein.
    * Hier geben wir das Trennzeichen ein, das OpenRefine zum Verbinden der Werte verwenden soll.
* Klicke auf "OK", um die Autorenzellen wieder zusammenzufügen.

Du siehst jetzt, dass die geteilten Zeilen verschwunden sind - die Autoren wurden mit dem angegebenen Trennzeichen zu einer einzigen Zelle verbunden. Unsere Zeilen- und
Records sind nun gleich, da wir keine Spalten mit geteilten (mehrwertigen) Zellen mehr haben.

* Klicke auf die Optionen "Zeilen" und "Datensätze" und beobachte, wie die Anzahl der Zeilen und Datensätze gleich ist.

### Auswahl eines guten Trennzeichens

Die Wahl eines guten Trennzeichen ist wichtig. In den Beispielen haben wir gesehen, dass das Pipe-Zeichen ( \| ) verwendet wurde.

Die Wahl des falschen Trennzeichens kann zu Problemen führen. Betrachte das folgende Beispiel für einen mehrwertigen Autor,
mit einer Pipe als Trennzeichen.
```
Jones, Andrew | Davis, S.
```

Wenn wir OpenRefine anweisen, diese Zelle an der Pipe ( \| ) aufzuteilen, erhalten wir die folgenden zwei Autoren in jeweils einer eigenen Zelle, da sie durch ein einzelnes Pipe-Zeichen getrennt sind.

- **Autor 1:** Jones, Andrew
- **Autor 2:** Davis, S.

Stell dir nun vor, der Ersteller des Dokuments hätte als Trennzeichen ein **Komma** statt einer Pipe gewählt.

```
Jones, Andrew , Davis, S.
```

Kannst du das Problem erkennen? Kannst du erkennen, wo ein Autor aufhört und der nächste beginnt?  

OpenRefine trennt bei **jedem** Komma, auf das es trifft,
Am Ende haben wir also 4 Autoren und nicht zwei, weil OpenRefine nicht erkennen kann, dass **Jones, Andrew** ein einzelner Autor sein soll. Wir erhalten
die folgenden vier "Autoren", weil die Namensteile durch 3 Kommas voneinander getrennt sind.

- **Autor 1:** Jones
- **Autor 2:** Andrew
- **Autor 3:** Davis
- **Autor 4:** S.

Die Aufteilung durch ein Komma funktioniert bei Authors nicht, weil die Namen Kommas enthalten können.

> ## Wähle ein Trennzeichen, das nicht in deinen Datenwerten enthalten ist
>
> Wenn du ein Arbeitsblatt mit mehrwertigen Zellen erstellst, ist es wichtig, ein Trennzeichen zu wählen, das nicht in den
> den Zellwerten selbst vorkommt. Aus diesem Grund ist das Pipe-Zeichen ( \| ) oft eine gute Wahl, da es
> selten in Daten verwendet wird. Kommas, Doppelpunkte und Semikolons sollten als Trennzeichen vermieden werden.
{>##}

>## Aufteilung von Fächern in separate Zellen
>
>1. Welches Trennzeichen wird in den Zellen für die Subjects verwendet?
>2. wie würdest du diese Themen in einzelne Zellen aufteilen?
>
> > ## Lösung
> > 1. Die Themenwörter/-überschriften werden mit dem Pipe-Zeichen ( \| ) aufgeteilt
> > 2. Um die Betreffwörter in einzelne Zellen aufzuteilen, musst du:
> > * Klicke auf das Dropdown-Menü oben in der Spalte "Betreffs".
> > * Wähle "Zellen bearbeiten->Mehrwertige Zellen aufteilen".
> > * Gib in der Eingabeaufforderung das (\| ) Symbol ein und klicke auf "OK".
> {: .Lösung}
{.challenge}

>## Die Spalte "Themen" wieder zusammenfügen
>
>1. Verbinde nun die Themen mit Hilfe des Gelernten wieder zusammen
>
> > ## Lösung
> > 1. Die Betreff-Wörter/Überschriften wurden zuvor mit dem Pipe-Zeichen ( \| ) abgegrenzt
> > 2. Um die geteilten Betreff-Zellen wieder zu einer einzigen Zelle zu verbinden, musst du:
> > * Klicke auf das Dropdown-Menü oben in der Spalte "Betreffs".
> > * Wähle "Zellen bearbeiten->Mehrwertige Zellen verbinden".
> > * Gib in der Eingabeaufforderung das (\| ) Symbol ein und klicke auf "OK".
> {: .Lösung}
{: .challenge}
