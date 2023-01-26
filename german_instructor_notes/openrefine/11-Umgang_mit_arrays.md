---
Titel: "Transformationen - Umgang mit Arrays"
Unterricht: 5
Übungen: 15
Fragen:
- "Wie verwende ich Arrays bei der Datentransformation?"
Ziele:
- "Verstehe den Zweck von Arrays in OpenRefine"
- "Arrays als Teil von Transformationen in GREL verwenden"
Kernpunkte:
- "Arrays können nicht direkt in einer OpenRefine-Zelle erscheinen"
- "Arrays können auf viele Arten mit GREL-Ausdrücken verwendet werden"
---

## Arrays
Ein "Array" ist eine Liste von Werten, die in Refine durch die Verwendung von eckigen Klammern dargestellt wird, 
die eine Liste von Werten enthalten, die durch Kommas getrennt sind. Ein Array, 
das die Wochentage auflistet, sieht zum Beispiel so aus:

["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

Arrays können in GREL-Ausdrücken sortiert, von Duplikaten befreit und auf andere Weise manipuliert werden, 
aber sie können nicht direkt in einer OpenRefine-Zelle erscheinen. Arrays in OpenRefine sind normalerweise 
das Ergebnis einer Transformation. Die Funktion ``Split`` zum Beispiel nimmt eine Zeichenkette und wandelt sie 
mit Hilfe eines Trennzeichens in ein Array um. Wenn eine Zelle zum Beispiel den Wert hat:

"Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag"

Dies kann mit der Funktion ```split`` in ein Array umgewandelt werden
```
value.split(",")
```
Dies würde ein Array mit den Wochentagen erzeugen:

["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

Dies kann mit Array-Operationen wie ``sort`` kombiniert werden. Angenommen, die Zelle enthält denselben Wert wie oben, dann kann die Funktion
```
value.split(",").sort()
```
ein Array ergeben, das die Wochentage in alphabetischer Reihenfolge enthält:

["Freitag", "Montag", "Samstag", "Sonntag", "Donnerstag", "Dienstag", "Mittwoch"]

Um einen Wert aus einem Array auszugeben, kannst du entweder einen bestimmten Wert abhängig von seiner Position in der Liste auswählen 
(wobei die erste Position als "Null" behandelt wird). Zum Beispiel
```
value.split(",")[0]
```
würde den ersten Wert aus dem Array extrahieren, das durch die Funktion ```split``` erstellt wurde. Im obigen Beispiel wäre das "Monday".

Du kannst auch Arrays miteinander verbinden, um einen "String" zu erstellen. Der GREL-Ausdruck würde wie folgt aussehen
```
value.split(",").sort().join(",")
```
Um das obige Beispiel noch einmal aufzugreifen, würde dies einen String ergeben, der die Wochentage in alphabetischer 
Reihenfolge und mit Kommas zwischen den einzelnen Tagen auflistet.

>## Autorennamen umkehren

>In dieser Übung werden wir sowohl den booleschen als auch den Array-Datentyp verwenden.
>Wenn du dir die Spalte Autoren ansiehst, kannst du sehen, dass die meisten Autorennamen in der Reihenfolge der Vornamen geschrieben sind. 
>Bei einigen wenigen wurde die Reihenfolge jedoch umgedreht, so dass der Familienname an erster Stelle steht.

>Nachdem wir die Zeilen mit einem Komma im Namen eingegrenzt haben, können wir die GREL-Funktion ```split`` verwenden. Diese Funktion unterscheidet sich von der Operation ``Split multi-valued cells``, die wir zuvor verwendet haben, da sie uns erlaubt, den Inhalt einer Zelle zu manipulieren, anstatt neue Zellen zu erstellen.
>
>1. Wähle in der Spalte ``Autoren`` das Dropdown-Menü und wähle ``Edit cells->Transform``.
>2. im Feld Ausdruck gibst du ```value.split(", ")``` ein (achte darauf, dass du nach dem Komma im Split-Ausdruck ein Leerzeichen einfügst, damit du später keine zusätzlichen Leerzeichen in deinem Autorennamen hast).
>3. sieh dir an, wie dadurch ein Array mit zwei Elementen in jeder Zeile in der Spalte "Vorschau" entsteht
>
>Um den Autorennamen in der Reihenfolge des persönlichen Namens zu erhalten, kannst du das Array umkehren und mit einem Leerzeichen wieder zusammenfügen, um die benötigte Zeichenfolge zu erstellen:
>
>1. Füge im Feld "Expression " zum bestehenden Ausdruck hinzu, bis er lautet: ```value.split(", ").reverse().join(" ")```
>2. in der Vorschau solltest du sehen können, dass das Array umgekehrt und wieder zu einem String verbunden wurde
>* Klicke auf ```OK``
{: .checklist}
