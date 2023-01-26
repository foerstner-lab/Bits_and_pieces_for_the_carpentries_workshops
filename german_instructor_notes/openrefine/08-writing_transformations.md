---
Titel: "Writing Transformations"
Unterricht: 5
Übungen: 10
Fragen:
- "Wo schreibe ich GREL-Ausdrücke in der OpenRefine-Schnittstelle?"
- "Wie schreibe ich einen gültigen GREL-Ausdruck?"
Ziele:
- "Erklären, wie man eigene Transformationen mit GREL schreibt"
Kernpunkte:
- "Du kannst Daten in OpenRefine auf der Grundlage bestimmter Anweisungen verändern.
- "Du kannst die Ergebnisse deines GREL-Ausdrucks in der Vorschau anzeigen"
---

## Transformationen schreiben

Um mit dem Schreiben von Transformationen zu beginnen, markierst du die Spalte, für die du eine Transformation durchführen möchtest, 
und wählst ``Edit cells->Transform… ```. In dem daraufhin angezeigten Fenster hast du die Möglichkeit, eine Transformation 
zu schreiben (das Feld "Ausdruck") und eine Vorschau der Auswirkungen der Transformation auf 10 Zeilen deiner Daten anzuzeigen.

Die Transformation, die du in das Feld "Ausdruck" eingibst, muss ein gültiger GREL-Ausdruck sein. 
Der Standardausdruck ist das Wort "value" selbst - das bedeutet, dass der aktuelle Wert in der Spalte steht, d.h. keine Änderung.

GREL-Funktionen werden geschrieben, indem du einer GREL-Funktion einen Wert gibst (eine Zeichenkette, ein Datum, eine Zahl usw.). 
Einige GREL-Funktionen benötigen zusätzliche Parameter oder Optionen, die bestimmen, wie die Funktion arbeitet. 
GREL unterstützt zwei Arten von Syntax:

- value.function(options)
- function(value, options)

Beide sind gültig, und welche davon verwendet wird, hängt ganz von den persönlichen Vorlieben ab. 

Neben der Option "Preview" gibt es Optionen zum Anzeigen:

* "History" - eine Liste der Transformationen, die du bereits verwendet hast, mit der Option, sie sofort wiederzuverwenden oder sie für einen leichteren Zugriff zu "markieren".
* "Starred" - eine Liste der Transformationen, die du in der Ansicht "Verlauf" mit einem Sternchen versehen hast
* Help" - eine Liste aller GREL-Funktionen und kurze Informationen zu ihrer Verwendung

>## Titel in Großbuchstaben setzen
>Verwende Facetten und den GREL-Ausdruck ```Wert.toTitlecase()```, um die Titel in Title Case zu setzen
>1. Facette nach publisher
>2. wähle "Akshantala Enterprises" und "Society of Pharmaceutical Technocrats" aus
>3. um mehrere Werte in der Facette auszuwählen, benutze den Link ``include ```, der rechts neben der Facette erscheint
>4. Achte darauf, dass die Titel alle in Großbuchstaben geschrieben sind.
>5.  Klicke auf das Dropdown-Menü in der Spalte Title
>6. wähle ``Edit cells->Transform...``.
>7. gib in das Feld Ausdruck ``value.toTitlecase()`` ein.
>8. im Vorschaufenster unter value.toTitlecase()  kannst du sehen, wie sich die Ausführung auswirkt
>9. Klicke auf ```OK```
{: .checklist}
