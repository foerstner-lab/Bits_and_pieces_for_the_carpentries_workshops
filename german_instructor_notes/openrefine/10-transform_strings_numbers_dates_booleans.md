---
Titel: "Transforming Strings, Numbers, Dates and Booleans"
Unterricht: 5
Übungen: 15
Fragen:
- "Wie verwende ich Transformationen, um meine Daten programmatisch zu bearbeiten?"
- "Wie transformiere ich die verschiedenen Datentypen?"
Ziele:
- "Benenne und beschreibe 4 Datentypen - String, Zahl, Datum und Boolesche Werte"
- "Daten für weitere Analysen umwandeln"
- Boolesche Daten verwenden, um Informationen zu identifizieren, die in einem anderen Format aufgezeichnet wurden.
- Boolesche Werte erstellen und umwandeln.
Stichpunkte:
- "Du kannst Daten in OpenRefine basierend auf bestimmten Anweisungen verändern"
- "Du kannst die in OpenRefine eingebauten Datenbearbeitungsfunktionen erweitern, indem du deine eigenen erstellst"
---

## Datentypen
Wenn du die Datentypen verstehst, kannst du mit GREL eine größere Vielfalt an Transformationen schreiben.

>## Datentypen in OpenRefine
>Jedes Datenelement in OpenRefine hat einen "type". Der gebräuchlichste "type" ist ein "string" - also ein Stück Text. Es gibt jedoch auch andere Datentypen, und mit Hilfe von Transformationen kannst du Daten von einem Typ in einen anderen umwandeln, wenn dies sinnvoll ist. Die unterstützten Datentypen sind:
>
>* Zeichenkette/Strings
>* Zahl/number
>* Datum/date
>* Boolesch/Boolean
>* Array (wird in der nächsten Lektion behandelt) /Feld,Reihe
{: .callout}

### Daten und Zahlen
Bisher haben wir uns nur mit Daten vom Typ "String" beschäftigt. In den meisten Fällen ist es möglich, Zahlen und Daten als Strings zu behandeln. 
In der Spalte Datum wird zum Beispiel das Datum der Veröffentlichung als String dargestellt. Einige Operationen und Transformationen funktionieren 
jedoch nur bei Daten vom Typ "number" oder "date", z. B. das Sortieren von Werten in numerischer oder datumsbezogener Reihenfolge. 
Um diese Funktionen auszuführen, müssen wir die Werte zunächst in ein Datum oder eine Zahl umwandeln.

>## Das Datum umformatieren
>1. Stelle sicher, dass du alle Facetten und Filter entfernst.
>2. in der Spalte "Date" wählst du aus dem Dropdown-Menü "Edit cells -> Transform".
>2. gib in das Feld "Expression" den GREL-Ausdruck ```value.toDate("dd/MM/yyyy")`` ein und drücke OK.
>3. beachte, dass die Werte jetzt grün angezeigt werden und einem Standardformat (ISO 8601) entsprechen - das bedeutet, dass sie jetzt als Datumsdatentyp in OpenRefine gespeichert sind. Wir können nun Funktionen ausführen, die speziell für Datumsangaben gelten
>4. in der Dropdown-Liste der Datumsspalten wählst du ``Edit column->Add column based on this column``. Mit dieser Funktion kannst du eine neue Spalte erstellen, während die alte Spalte erhalten bleibt
>5. Im Feld "New column name" gibst du "Formatted-Date" ein.
>6. in das Feld 'Expression' gibst du den GREL-Ausdruck ```value.toString(“dd MMMM yyyy”)```
{: .checklist}

>## Festlegen der Datumsformatierung in GREL-Ausdrücken
>
>GREL erlaubt es uns, Datum und Uhrzeit mit Hilfe von ```Pattern Strings`` anzugeben, das sind Buchstaben, die eine bestimmte Darstellung im Funktionsaufruf haben.
>
Bei >Pattern Strings wird zwischen Groß- und Kleinschreibung unterschieden, daher haben Groß- und Kleinbuchstaben eine unterschiedliche Bedeutung und Verwendung.
{: .callout}

Die folgende Tabelle zeigt Buchstaben, die sich auf die Darstellung von Datum und Uhrzeit beziehen.

| Buchstabe| Datums- oder Zeitdarstellung |
| ------------- |:-------------:|
| `y` | Jahr|
| "M" | Monat im Jahr|
| "D" | Tag im Jahr|
| "d" | Tag im Monat|
| "F" | Wochentag im Monat|
| `E` | Tagesname in Woche|
| "u" | Tagesnummer in der Woche|
| "a" | AM/PM-Marker|

Die folgende Tabelle zeigt Beispiele für die Verwendung der Muster als Eingabe und die daraus resultierende Ausgabe.

| Datum- und Zeitmuster Eingabe | Ausgabe |
| ------------- |:-------------:|
| "jjjj-MM-tt"| 2022-06-05|
| "tt MMM jjjj"| 05 Jun 2022|
| `"EEE, MMM d, ''yy"`| Mon, Jun 5, '22|
| "jjjj.MMMM.tt hh:mm a"`| 2022.Juni.05 12:10 PM|
| `"EEE, d MMM yyyy HH:mm:ss"`| Mon, 5 Jun 2022 12:10:10|

Eine ausführlichere Erklärung findest du in der [OpenRefine Dokumentation](https://docs.openrefine.org/manual/grelfunctions#date-functions).


### Boolesche Werte
Ein "Boolean" ist ein binärer Wert, der entweder "wahr" oder "falsch" sein kann. 
Boolesche Werte können direkt in OpenRefine-Zellen verwendet werden, werden aber häufiger in Transformationen 
als Teil eines GREL-Ausdrucks verwendet. Zum Beispiel der GREL-Ausdruck
```
value.contains("test")
```
erzeugt einen booleschen Wert von entweder "true" oder "false", je nachdem, ob der aktuelle Wert in der Zelle irgendwo den Text "test" enthält.

Solche Tests können mit anderen GREL-Ausdrücken kombiniert werden, um komplexere Umwandlungen zu erstellen. 
Zum Beispiel, um eine weitere Transformation nur dann auszuführen, wenn ein Test erfolgreich ist. 
Die GREL-Transformation ```if(value.contains("test"),"Test data",value)``` ersetzt einen Zellenwert nur dann mit den Worten "Testdaten", 
*wenn* der Wert in der Zelle irgendwo die Zeichenfolge "test" enthält.

>## Umgekehrte Autorennamen finden
>In dieser Übung verwenden wir den booleschen Datentyp.
>Wenn du dir die Spalte "Autoren" ansiehst, kannst du sehen, dass die meisten Autorennamen mit dem persönlichen Namen zuerst geschrieben werden. Bei einigen wenigen wurde der Familienname jedoch umgedreht und steht nun an erster Stelle.
>
>Wir können einen groben Test für umgekehrte Autorennamen durchführen, indem wir nach Namen suchen, die ein Komma enthalten:
>
>1. Vergewissere dich, dass du die Autorennamen bereits mit ```Edit cells->Split multi-valued cells``` in einzelne Zellen aufgeteilt hast (das solltest du in Übung 5 gemacht haben)
>2. in der Spalte "Autoren" wählst du im Dropdown-Menü "Facet->Custom text facet..." aus.
>3 Mit der Funktion Custom text facet kannst du GREL-Funktionen schreiben, um eine Facette zu erstellen.
>4. in das Feld Ausdruck gibst du ```value.contains(",")``` ein.
>* Klicke auf ```OK``
>* Da die Funktion "contains" einen booleschen Wert ausgibt, solltest du eine Facette sehen, die "falsch" und "wahr" enthält. Diese stehen für das Ergebnis des Ausdrucks, d.h. true = Werte, die ein Komma enthalten; false = Werte, die kein Komma enthalten
>* Um die Namen in die Reihenfolge der Personennamen zu ändern, siehe die Lektion Arrays.
{: .checklist}
