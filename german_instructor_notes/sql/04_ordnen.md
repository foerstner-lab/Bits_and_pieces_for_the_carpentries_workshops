---
Titel: "Ordnen"
Unterricht: 15
Übungen: 0
Fragen:
- "Wie ist die Reihenfolge der Ausführung bei SQL-Abfragen?
- "Wie können Sie komplexere SQL-Abfragen organisieren und kommentieren?"
Ziele:
- "Verstehen, wie man Abfragen erstellt, und die Reihenfolge, in der die Teile erstellt werden.
Schlüsselpunkte:
- "Abfragen haben oft die Struktur: SELECT data FROM table WHERE bestimmte Kriterien vorhanden sind". 
---

## Reihenfolge der Ausführung

Nehmen wir an, wir hätten die folgende Frage:

~~~
SELECT Title, Author
FROM articles
WHERE ISSNs = '2067-2764|2247-6202'.
ORDER BY First_Author ASC;
~~~
{: .sql}

Interessant an dieser Abfrage ist, dass wir nicht unbedingt die Spalte `Erster_Autor` in unseren Ergebnissen anzeigen müssen, um nach ihr zu sortieren. 

Wir können dies tun, weil die Sortierung früher in der Berechnungs-Pipeline als die Feldauswahl erfolgt.

> ## Der Computer macht das im Grunde genommen:
>
> 1. Filtern von Zeilen nach WHERE
> 2. Sortierung der Ergebnisse nach ORDER BY
> 3. angeforderte Spalten oder Ausdrücke anzeigen.
>
{: .callout}

Es ist möglich, eine Abfrage als eine einzige Zeile zu schreiben, aber aus Gründen der Lesbarkeit empfehlen wir, jeden Abschnitt in eine eigene Zeile zu setzen.

## Komplexe Abfragen

Betrachten Sie die folgende Abfrage:

~~~
SELECT *
FROM articles
WHERE (ISSNs = '2076-0787') OR (ISSNs = '2077-1444') OR (ISSNs = '2067-2764|2247-6202');
~~~
{: .sql}

SQL bietet die Flexibilität, neue Bedingungen iterativ hinzuzufügen, aber Sie können einen Punkt erreichen, an dem die Abfrage schwer zu lesen und ineffizient ist. Wir können zum Beispiel `IN` verwenden, um die Abfrage zu verbessern und lesbarer zu machen:

~~~
SELECT *
FROM articles
WHERE (ISSNs IN ('2076-0787', '2077-1444', '2067-2764|2247-6202'));
~~~
{: .sql}

Wir begannen mit etwas Einfachem, fügten dann nach und nach weitere Klauseln hinzu und testeten
ihre Auswirkungen, während wir weitermachten.  Bei komplexen Fragen ist dies eine gute Strategie, um sicherzustellen, dass Sie bekommen, was Sie wollen.  Manchmal kann es helfen, eine Teilmenge der Daten, die Sie leicht in einer temporären Datenbank sehen können, zu nehmen, um Ihre Abfragen zu üben, bevor Sie an einer größeren oder komplizierteren Datenbank arbeiten.
