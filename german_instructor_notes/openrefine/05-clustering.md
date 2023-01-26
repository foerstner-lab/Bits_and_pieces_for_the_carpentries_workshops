---
Titel: "Clustering"
Unterricht: 10
Übungen: 10
Fragen:
- "Was ist Clustering in OpenRefine und wann würdest du es verwenden?"
- "Wie funktioniert das Clustering in OpenRefine?"
Ziele:
- "Erkläre, was Clustering in OpenRefine ist"
- Nutze das Clustering, um unterschiedliche Formen derselben Daten zu identifizieren und durch einen einzigen konsistenten Wert zu ersetzen.
Kernpunkte:
- "Clustering ist eine Methode, um verschiedene Formen derselben Daten in einem Datensatz zu finden (z.B. verschiedene Schreibweisen eines Namens)"
- Es gibt verschiedene Clustering-Algorithmen, die auf unterschiedliche Weise funktionieren und unterschiedliche Ergebnisse liefern.
- Welcher Clustering-Algorithmus am besten geeignet ist, hängt von den Daten ab.
- "Mit Clustering kannst du verschiedene Formen derselben Daten durch einen einzigen konsistenten Wert ersetzen"
---

## Clustering
Die Funktion Cluster fasst ähnliche, aber inkonsistente Werte in einer bestimmten Spalte zusammen und ermöglicht es dir, 
diese inkonsistenten Werte zu einem einzigen Wert deiner Wahl zusammenzufassen.

Das ist sehr effektiv, wenn du Daten mit geringfügigen Abweichungen in den Datenwerten hast, z. B. Namen von Personen, 
Organisationen, usw.

Um die Funktion "Clustern" zu verwenden, klickst du auf die Menüoption "Zellen bearbeiten" in der entsprechenden Spalte und wählst 
"Clustern und bearbeiten...".

Die "Cluster" werden automatisch nach einem Algorithmus erstellt. OpenRefine unterstützt eine Reihe verschiedener Clustering-Algorithmen - 
es kann sein, dass du ein wenig experimentieren musst, um herauszufinden, welcher Clustering-Algorithmus bei einem bestimmten Datensatz 
am besten funktioniert, und du wirst feststellen, dass verschiedene Algorithmen unterschiedliche Cluster hervorheben.

Weitere Informationen zu den Methoden, die zur Erstellung von Clustern verwendet werden, findest du unter [https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth](https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth)

Für jeden Cluster hast du die Möglichkeit, die Werte "zusammenzuführen" - das heißt, die verschiedenen inkonsistenten Werte durch 
einen einzigen konsistenten Wert zu ersetzen. Standardmäßig verwendet OpenRefine den häufigsten Wert im Cluster als neuen Wert, 
aber du kannst auch einen anderen Wert auswählen, indem du auf den Wert selbst klickst, oder du kannst den gewünschten Wert in das Feld 
"New Cell Value" eingeben.

>## Clustering verwenden, um Autorendaten zu bereinigen
>
>1. Teile die Autorennamen mit "Zellen bearbeiten -> Mehrwertige Zellen aufteilen" in einzelne Zellen auf und verwende das Pipe-Zeichen als Trennzeichen.
>2. wähle "Zellen bearbeiten -> Clustern und bearbeiten" in der Spalte "Autor".
>3. verwende die Methode "Schlüsselkollision" mit der Funktion "Fingerabdruck", um die Wertecluster zu bearbeiten und sie gegebenenfalls zu einem einzigen Wert zusammenzufassen
>4. versuche, die verwendete Clustermethode zu ändern - welche funktioniert gut?
{: .challenge}
