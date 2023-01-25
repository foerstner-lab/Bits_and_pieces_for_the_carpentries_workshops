---
Titel: "Layout von OpenRefine, Zeilen vs. Datensätze"
Unterricht: 10
Übungen: 5
Fragen:
- "Wie sind die Daten in OpenRefine organisiert?"
- Wie erhalte ich Zugang zu den Optionen zur Änderung von Daten in OpenRefine?
- "Was ist der Unterschied zwischen Zeilen und Datensätzen in OpenRefine?"
- Wie kann ich mit einzelnen Zellen arbeiten, die mehrere Werte in einer Liste enthalten?
Ziele:
- Steuerelemente zum Navigieren in OpenRefine finden
- Optionen für die Arbeit mit Daten über die OpenRefine-Dropdown-Menüs finden
- Zellen, die mehrere Daten enthalten, so aufteilen, dass sich jedes Datenelement in einer eigenen Zelle befindet
Schlüsselpunkte:
- "OpenRefine verwendet Zeilen und Spalten zur Anzeige von Daten"
- Die meisten Optionen für die Arbeit mit Daten in OpenRefine werden über ein Dropdown-Menü am oberen Rand einer Datenspalte aufgerufen.
- Wenn Sie eine Option in einer bestimmten Spalte auswählen (z. B. um eine Änderung an den Daten vorzunehmen), wirkt sich dies auf alle Zellen in dieser Spalte aus.
- OpenRefine verfügt über einen Datensatzmodus, der mehrere Zeilen zu einem einzigen Datensatz zusammenfasst.
- Teilen und Verbinden von mehrwertigen Zellen, um die einzelnen Werte darin zu ändern.
- "Wählen Sie beim Erstellen von mehrwertigen Zellen in Ihren Daten ein Trennzeichen, das nicht in den Datenwerten erscheint"
---

## Das Layout von OpenRefine
OpenRefine zeigt die Daten in einem Tabellenformat an. Jede Zeile stellt normalerweise einen "Datensatz" in den Daten dar, während jede Spalte eine Art von Information repräsentiert. Dies ist der Darstellung von Daten in einer Tabellenkalkulation oder Datenbank sehr ähnlich. Wie bei einer Tabellenkalkulation befinden sich die einzelnen Datenbits in "Zellen" an der Schnittstelle zwischen einer Zeile und einer Spalte.

OpenRefine zeigt nur eine begrenzte Anzahl von Datenzeilen auf einmal an. Sie können die Anzahl zwischen 5, 10 (Standard), 25 und 50 oben links in der Datentabelle einstellen. Sie können durch die Datensätze navigieren, indem Sie die Navigationsoptionen Vorherige/Nächste/Erste/Letzte oben rechts in der Datentabelle verwenden.

In OpenRefine ist es jederzeit möglich, Änderungen rückgängig zu machen: Beachten Sie das linke Feld, das derzeit leer ist. Lesen Sie die vier Wörter am oberen Rand des Fensters:
Facette/Filter und Rückgängig/Redo.  Auf die Undo/Redo-Befehle werden wir uns im weiteren Verlauf des Workshops konzentrieren; Sie können sie bei Bedarf jederzeit verwenden. 

## Arbeiten mit Daten in OpenRefine
Die meisten Optionen für die Arbeit mit Daten in OpenRefine werden über Dropdown-Menüs am oberen Rand der Datenspalten aufgerufen. Wenn Sie eine Option in einer bestimmten Spalte auswählen (z. B. um eine Änderung an den Daten vorzunehmen), wirkt sich dies auf alle Zellen in dieser Spalte aus. Wenn Sie Änderungen in mehreren Spalten vornehmen möchten, müssen Sie dies spaltenweise tun.

## Zeilen und Datensätze
OpenRefine verfügt über zwei Modi zur Anzeige von Daten: 'Zeilen' und 'Datensätze'. Im Moment befinden wir uns im Modus "Zeilen", in dem jede Zeile einen einzelnen Datensatz darstellt - in diesem Fall einen Artikel. Im Modus "Datensätze" kann OpenRefine mehrere Zeilen miteinander verknüpfen, so dass sie zum selben Datensatz gehören. Zeilen werden anhand der Werte in der ersten Spalte den Datensätzen zugeordnet. Siehe mehr [Details zu Zeilen und Datensätzen in der OpenRefine-Dokumentation](https://docs.openrefine.org/manual/exploring#rows-vs-records).

### Zellen aufteilen

Um zu sehen, wie dies in der Praxis funktioniert, können wir die Autorennamen in separate Zellen aufteilen. Wenn Sie sich die Autorenspalte ansehen, sollten Sie erkennen können, dass sich in jeder Zelle mehrere Namen befinden, die durch das Pipe-Symbol ( \| ) getrennt sind.

Um mit den Autorennamen in OpenRefine effektiv arbeiten zu können, müssen wir jeden Namen in einer eigenen Zelle haben. Um die Namen in ihre eigenen Zellen aufzuteilen, können wir die Funktion `Split multi-valued cells` verwenden:

* Klicken Sie auf das Dropdown-Menü oben in der Spalte "Autor".
* Wählen Sie "Zellen bearbeiten->Mehrwertige Zellen aufteilen".
* Geben Sie in der Eingabeaufforderung das Symbol ( \| ) ein und klicken Sie auf "OK".
    * Beachten Sie, dass die Zeilen weiterhin fortlaufend nummeriert sind.
* Klicken Sie auf die Option "Datensätze", um in den Modus "Datensätze" zu wechseln.
    * Beachten Sie, dass sich die Nummerierung geändert hat, was darauf hinweist, dass sich mehrere Zeilen auf denselben Datensatz beziehen.

 Bildschirmfoto von OpenRefine im Modus "Zeilen" (../assets/img/rows.png)
 Bildschirmfoto von OpenRefine im Zeilenmodus (../assets/img/records.png)

Beachten Sie in den obigen Bildern den Unterschied zwischen: Zeilen mit demselben Titel erscheinen unter jedem gemeinsamen Titel, wobei die nummerierte Reihenfolge in der dritten Spalte von links unterbrochen wird. Gemeinsame Titel haben die gleiche Schattierung, was visuell sehr schwer zu unterscheiden sein kann. Achten Sie daher auf die Sterne und Fähnchen in den Spalten ganz links, die eine neue Zeile, d. h. einen Artikel mit einem anderen Autor, anzeigen.

Da wir nun in der Lage sind, Zellen mit mehreren Werten aufzuteilen, werden wir uns nun damit beschäftigen, wie man sie wieder zusammenfügt.

### Zellen zusammenfügen

Ein üblicher Arbeitsablauf mit mehrwertigen Zellen ist

- Aufteilung mehrwertiger Zellen in einzelne Zellen (wie oben)
- Ändern/Verfeinern/Säubern einzelner Zellen
- Zusammenfügen mehrwertiger Zellen

Das Ändern von Zellen wird in späteren Lektionen behandelt, aber jetzt werden wir uns damit befassen, wie man Zellen, die zuvor aufgeteilt wurden, wieder zusammenfügt.

* Klicken Sie auf das Dropdown-Menü oben in der Autorenspalte.
* Wählen Sie "Zellen bearbeiten->Mehrwertige Zellen verbinden".
* Geben Sie in der Eingabeaufforderung das Symbol ( \| ) ein.
    * Hier geben wir das Trennzeichen ein, das OpenRefine zum Verbinden der Werte verwenden soll.
* Klicken Sie auf "OK", um die Autorenzellen wieder zusammenzufügen.

Sie sehen nun, dass die geteilten Zeilen verschwunden sind - die Authors wurden in einer einzigen Zelle mit dem angegebenen Trennzeichen zusammengefügt. Unsere Rows und
Records sind nun gleich, da wir keine Spalten mit geteilten (mehrwertigen) Zellen mehr haben.

* Klicken Sie auf die Optionen "Zeilen" und "Datensätze" und beobachten Sie, wie die Anzahl der Zeilen und Datensätze gleich ist.

### Auswahl eines guten Trennzeichens

Der Wert, der mehrwertige Zellen trennt, wird als Trennzeichen oder Delimiter bezeichnet. Die Wahl eines guten
Trennzeichen ist wichtig. In den Beispielen haben wir gesehen, dass das Pipe-Zeichen ( \| ) verwendet wurde.

Die Wahl des falschen Trennzeichens kann zu Problemen führen. Betrachten Sie das folgende Beispiel eines mehrwertigen Autors,
mit einer Pipe als Trennzeichen.
```
Jones, Andrew | Davis, S.
```

Wenn wir OpenRefine anweisen, diese Zelle an der Pipe ( \| ) aufzuteilen, erhalten wir die folgenden zwei Autoren jeweils in ihrer eigenen Zelle, da sie durch ein einzelnes Pipe-Zeichen getrennt sind.

- **Autor 1:** Jones, Andrew
- **Autor 2:** Davis, S.

Stellen Sie sich nun vor, der Ersteller des Dokuments hätte anstelle der Pipe ein **Komma** als Trennzeichen gewählt.

```
Jones, Andrew , Davis, S.
```

Können Sie das Problem erkennen? Können Sie erkennen, wo ein Autor aufhört und der nächste beginnt?  

OpenRefine trennt bei **jedem** Komma, auf das es trifft,
Am Ende haben wir also 4 Autoren, nicht zwei, weil OpenRefine nicht erkennen kann, dass **Jones, Andrew** ein einzelner Autor sein soll. Wir erhalten
die folgenden vier "Autoren", weil die Namensteile durch 3 Kommas getrennt sind.

- **Autor 1:** Jones
- **Autor 2:** Andrew
- **Autor 3:** Davis
- **Autor 4:** S.

Die Aufteilung durch ein Komma funktioniert bei Authors nicht, da die Namen Kommas enthalten können.

> ## Wählen Sie ein Trennzeichen, das nicht in Ihren Datenwerten enthalten ist.
>
> Bei der Erstellung eines Arbeitsblatts mit mehrwertigen Zellen ist es wichtig, ein Trennzeichen zu wählen, das niemals in
> den Zellwerten selbst vorkommt. Aus diesem Grund ist das Pipe-Zeichen ( \| ) oft eine gute Wahl, da es
> selten in Daten verwendet wird. Kommas, Doppelpunkte und Semikolons sollten als Trennzeichen vermieden werden.
{>##}

>## Aufteilung von Fächern in einzelne Zellen
>
>1. Welches Trennzeichen wird in den Zellen für die Themen verwendet?
>2. wie würden Sie diese Themen in einzelne Zellen aufteilen?
>
> > ## Lösung
> > 1. Die Themenwörter/-überschriften werden mit dem Pipe-Zeichen ( \| ) aufgeteilt.
> > 2. Um die Betreffwörter in einzelne Zellen aufzuteilen, müssen Sie Folgendes tun:
> > * Klicken Sie auf das Dropdown-Menü oben in der Spalte "Betreff".
> > * Wählen Sie "Zellen bearbeiten->Mehrwertige Zellen aufteilen".
> > * Geben Sie in der Eingabeaufforderung das Symbol (...) ein und klicken Sie auf "OK".
> {: .Lösung}
{: .challenge}

>## Die Spalte "Themen" wieder zusammenfügen
>
>1. Verbinden Sie nun die Themen mit Hilfe des Gelernten wieder miteinander
>
> > ## Lösung
> > 1. Die Schlagwörter/Überschriften wurden zuvor mit dem Pipe-Zeichen ( \| ) getrennt.
> > 2. Um die geteilten Betreffzellen wieder zu einer einzigen Zelle zu verbinden, müssen Sie Folgendes tun:
> > * Klicken Sie auf das Dropdown-Menü oben in der Spalte "Betreff".
> > * Wählen Sie "Zellen bearbeiten->Mehrwertige Zellen verbinden".
> > * Geben Sie in der Eingabeaufforderung das Symbol (...) ein und klicken Sie auf "OK".
> {: .Lösung}
{: .challenge}
