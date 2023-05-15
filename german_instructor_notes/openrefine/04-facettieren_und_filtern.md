---
Titel: "Facettieren und Filtern"
Unterricht: 10
Übungen: 10
Fragen:
- "Was ist eine Facette in OpenRefine?"
- "Was ist ein Filter in OpenRefine?"
- Wie kann ich Filter und Facetten nutzen, um Daten in OpenRefine zu erkunden?
- Wie kann ich häufige Probleme in meinen Daten mit OpenRefine beheben?
Ziele:
- "Erkläre, was Facetten und Filter sind"
- Fragen zum Inhalt eines Datensatzes mit Facetten beantworten.
- Facetten und Filter verwenden, um mit einer Teilmenge von Daten zu arbeiten.
- Datenprobleme mit Hilfe eines Facets korrigieren"
Stichpunkte:
- "Du kannst Facetten und Filter verwenden, um deine Daten zu erkunden"
- "Du kannst Facetten und Filter nutzen, um mit einer Teilmenge von Daten in OpenRefine zu arbeiten"
- "Du kannst häufige Datenprobleme über ein Facet korrigieren"
---

## Facetten
Facetten sind eine der nützlichsten Funktionen von OpenRefine und können sowohl dabei helfen, 
einen Überblick über die Daten zu bekommen als auch die Konsistenz der Daten zu verbessern.

Ein "Facet" gruppiert alle Werte, die in einer Spalte vorkommen, und ermöglicht es dir dann, 
die Daten nach diesen Werten zu filtern und Werte in vielen Datensätzen gleichzeitig zu bearbeiten.

Eine der am häufigsten verwendeten Facetten ist die sogenannte "Textfacette". Diese gruppiert alle 
Textwerte in einer Spalte und listet jeden Wert mit der Anzahl der Datensätze auf, in denen er vorkommt. 
Die Facetteninformationen werden immer im linken Bereich der OpenRefine-Oberfläche angezeigt.

Um eine Textfacette für eine Spalte zu erstellen, klickst du auf das Dropdown-Menü oben in der Publisher-Spalte 
und wählst "Facette -> Textfacette". Die Facette wird dann im linken Fenster angezeigt.

Die Facette besteht aus einer Liste von Werten, die in den Daten verwendet werden. Du kannst die angezeigten Daten filtern, 
indem du auf eine dieser Überschriften klickst.

Du kannst mehrere Werte aus der Facette auf einmal in einen Filter einbeziehen, indem du die Option "Include " verwendest, 
die erscheint, wenn du mit der Maus über einen Wert in der Facette fährst.

Du kannst den Filter auch "umkehren", um alle Datensätze anzuzeigen, die nicht mit den ausgewählten Werten übereinstimmen mit "invert". 
Diese Option wird oben im Facetten-Panel angezeigt, wenn du einen Wert aus der Facette auswählst, um ihn als Filter anzuwenden.

>## Erstellen wir eine Textfacette
>1. Klicke auf das Dropdown-Menü oben in der Verlagsspalte und wähle "Facette > Textfacette". Die Facette wird dann im linken Fenster angezeigt.
>2. um einen einzelnen Wert auszuwählen, klicke auf den Text der entsprechenden Zeile in der Facette
>3. um mehrere Werte auszuwählen, klicke auf die Option "Einschließen" in der entsprechenden Zeile der Facette (die nur erscheint, wenn du mit der Maus über die Zeile fährst)
>3. du kannst deine Auswahl "umkehren", um "auszuschließen".
>4. einen Wert einschließen und dann oben nachschauen, um die Einbeziehung umzukehren.
{: .checklist}

>## Welche Lizenzen werden für die Artikel in dieser Datei verwendet?
> Verwende eine "Textfacette" für die Spalte "Lizenz" und beantworte diese Fragen:
>
>1. Welches ist die am häufigsten verwendete Lizenz in der Datei?
>2. wie viele Artikel in der Datei haben keine Lizenz zugewiesen?
>
>>## Lösung
>>1. Erstelle eine Facette für die Spalte 'Licence'.
>>2. sortiere die Werte nach "Anzahl".
>>3. was ist die häufigste Lizenz in der Datei? Antwort: `CC BY`
>>4. wie viele Artikel in der Datei haben keine Lizenz zugeordnet? Antwort: **6**
>{: .solution}
{: .challenge}

## Filter
Du kannst nicht nur Facetten verwenden, um die in OpenRefine angezeigten Daten zu filtern, sondern auch "Textfilter" anwenden, 
die anhand einer eindeutigen Textzeichenfolge nach einem bestimmten Text in einer Spalte suchen, ähnlich wie eine Suchfunktion. 
Textfilter wendest du an, indem du auf das Dropdown-Menü oben in der Spalte klickst, auf die du den Filter anwenden möchtest, 
und "Textfilter" auswählst.

Wie bei den Facetten werden die Filteroptionen im linken Fenster von OpenRefine angezeigt. Wenn du den Text, den du für den Filter verwenden möchtest,
in das Textfeld des Filters eingibst, zeigt OpenRefine nur die Zeilen an, die diesen Text in der entsprechenden Spalte enthalten.

Du kannst auch [reguläre Ausdrücke](https://librarycarpentry.github.io/lc-data-intro/01-regular-expressions/) im Filter verwenden.

## Arbeiten mit gefilterten Daten
Wenn du die in OpenRefine angezeigten Daten gefiltert hast, ist es sehr wichtig zu wissen, dass alle Operationen, 
die du durchführst, nur auf die Zeilen angewendet werden, die dem Filter entsprechen - das sind die Daten, 
die gerade angezeigt werden. Um sicherzustellen, dass du mit den Daten arbeitest, die du auswählen wolltest, 
überprüfe die Anzahl der übereinstimmenden Datensätze, die über der Datentabelle angezeigt werden.

## Andere Arten von Facetten
Neben den "Text-Facetten" unterstützt OpenRefine auch eine Reihe anderer Facettentypen. Dazu gehören:

* Numerische Facetten
* Zeitleistenfacetten (für Daten)
* Scatterplot-Facetten
* Benutzerdefinierte Facetten


**Numerische und Zeitleisten-Facetten** zeigen Diagramme anstelle von Wertelisten an. Das Diagramm enthält Steuerelemente zum Ziehen und Ablegen, 
mit denen du einen Start- und Endbereich festlegen kannst, um die angezeigten Daten zu filtern.

Die **Scatterplot-Facetten** werden weniger häufig verwendet. 
Weitere Informationen dazu findest du im Tutorial unter [https://web.archive.org/web/20190105063215/http://enipedia.tudelft.nl/wiki/OpenRefine_Tutorial#Exploring_the_data_with_scatter_plots](https://web.archive.org/web/20190105063215/http://enipedia.tudelft.nl/wiki/OpenRefine_Tutorial#Exploring_the_data_with_scatter_plots).

**Benutzerdefinierte Facetten** sind eine Reihe verschiedener Arten von Facetten. Einige der standardmäßigen benutzerdefinierten Facetten sind:

* Wort-Facette - sie zerlegt den Text in Wörter und zählt die Anzahl der Datensätze, in denen jedes Wort vorkommt.
* Facette "Duplikate" - dies ergibt eine binäre Facette von "wahr" oder "falsch". Zeilen erscheinen in der Facette "wahr",  wenn der Wert in der ausgewählten Spalte genau mit einem Wert in derselben Spalte in einer anderen Zeile übereinstimmt
* Facette "Textlänge" - erstellt eine numerische Facette, die auf der Länge (Anzahl der Zeichen) des Textes in jeder Zeile der ausgewählten Spalte basiert. Dies kann nützlich sein, um falsche oder ungewöhnliche Daten in einem Feld zu erkennen, in dem bestimmte Längen erwartet werden (z. B. wenn die Werte voraussichtlich Jahre sind, ist jede Zeile mit einer Textlänge von mehr als 4 für diese Spalte wahrscheinlich falsch)
* Facette nach Leerzeichen - eine binäre Facette von "wahr" oder "falsch". Zeilen erscheinen in der Facette "wahr", wenn sie keine Daten in dieser Spalte enthalten. Dies ist nützlich, wenn du nach Zeilen suchst, in denen Schlüsseldaten fehlen.

OpenRefine begrenzt die Anzahl der Werte, die in einer Facette enthalten sein dürfen, um sicherzustellen, dass die Software nicht zu langsam arbeitet oder zu wenig Speicherplatz hat. 
Wenn du eine Facette mit vielen eindeutigen Werten erstellst (z. B. eine Facette für die Spalte "Buchtitel" in einem Datensatz mit einer Zeile pro Buch), wird die erstellte Facette sehr groß und kann entweder die Anwendung verlangsamen oder OpenRefine wird die Facette nicht erstellen.

>## Alle Publikationen ohne DOI finden
>* Verwende die Funktion "Facet by blank", um alle Publikationen in diesem Datensatz ohne DOI zu finden.
>
>>## Lösung
>>
>>1. Wähle in der Spalte "DOI" das Dropdown-Menü "Facetten > Angepasste Facetten > Facette nach Leerzeichen".
>>2. `True` bedeutet, dass sie leer ist, also kannst du:
>> * Wähle in der Facette `include` auf True, um die Liste der Publikationen auf diejenigen zu filtern, die kein DOI haben
>{: .solution}
{: .challenge}

## Ändern von Daten durch Facetten
Wenn du eine Textfacette erstellst, kannst du die Werte in der Facette bearbeiten, um den Wert für mehrere Datensätze gleichzeitig zu ändern. Dazu fährst du mit der Maus über den Wert, den du bearbeiten möchtest, und klickst auf die Option "Bearbeiten", die dann erscheint.

Diese Vorgehensweise ist bei relativ kleinen Facetten nützlich, bei denen es zu kleinen Abweichungen durch Zeichensetzung oder Tippfehler usw. kommen kann. Zum Beispiel bei einer Spalte, die nur Begriffe aus einer kleinen eingeschränkten Liste wie Wochentage oder Monate des Jahres enthalten soll.

Die Liste der Werte in der Facette wird aktualisiert, wenn du Änderungen vornimmst.

>## Korrigiere die Sprachwerte über eine Facette
>
>* Erstelle eine "Text-Facette" für die Spalte "Sprache" und korrigiere die Abweichungen bei den Werten "DE" und "Englisch".
>
>>## Lösung
>>1. Erstelle eine Text-Facette für die Spalte "Sprache".
>>2. bemerke, dass es sowohl `EN` als auch `English` gibt
>>3. fahre mit der Maus über den Wert "Englisch".
>>4. klicke auf "Bearbeiten".
>>5. Gib "EN" ein und klicke auf "Anwenden".
>>6. sieh zu, wie die Facette Sprache aktualisiert wird
>{: .solution}
{: .challenge}
