---
Titel: "Einführung in Transformationen"
Unterricht: 5
Übungen: 5
Fragen:
- "Wie verwende ich Transformationen, um meine Daten programmatisch zu bearbeiten?"
- "Welche Arten von Transformationen unterstützt Open Refine?"
- "Was ist GREL?"
Ziele:
- "Beschreibe gängige Transformationen"
- "Erkläre GREL, die General Refine Expression Language".
Stichpunkte:
- "Gängige Transformationen sind über die Menüoption verfügbar"
---

## Einführung in Transformationen

Mit Facetten, Filtern und Clustern bietet OpenRefine relativ einfache Möglichkeiten, 
sich einen Überblick über deine Daten zu verschaffen und Änderungen vorzunehmen. 

Manchmal möchtest du jedoch Änderungen an den Daten vornehmen, die sich auf diese Weise nicht erreichen lassen. 
Solche Änderungen sind zum Beispiel:

* Aufteilung von Daten aus einer einzigen Spalte in mehrere Spalten (z. B. Aufteilung einer Adresse in mehrere Teile)
* Standardisieren des Datenformats in einer Spalte, ohne die Werte zu ändern (z. B. Entfernen von Satzzeichen oder Standardisieren eines Datumsformats)
* Extrahieren eines bestimmten Datentyps aus einem längeren Text (z. B. Auffinden von ISBNs in einer bibliografischen Angabe)

Um diese Art von Aktivitäten zu unterstützen, unterstützt OpenRefine "Transformationen", d. h. Methoden zur Manipulation 
von Daten in Spalten. Transformationen werden normalerweise in einer speziellen Sprache namens "GREL" (General Refine Expression Language) 
geschrieben. In gewisser Weise ähneln GREL-Ausdrücke den Excel-Formeln, obwohl sie sich eher auf Textmanipulationen als auf numerische 
Funktionen konzentrieren.

Die vollständige Dokumentation für GREL findest du unter [https://docs.openrefine.org/manual/grelfunctions](https://docs.openrefine.org/manual/grelfunctions). In diesem Lernprogramm wird nur ein kleiner Teil der verfügbaren Befehle behandelt.

### Allgemeine Transformationen
Einige Transformationen werden regelmäßig verwendet und sind direkt über Menüoptionen zugänglich, ohne dass du sie direkt eingeben musst.

Beispiele für einige dieser häufig verwendeten Transformationen sind in der folgenden Tabelle aufgeführt, zusammen mit den entsprechenden
GREL-Befehlen. Wir werden später in dieser Lektion sehen, wie man die GREL-Version verwendet.

Allgemeine Umwandlung | Aktion | GREL-Ausdruck
--------------------| ------------- | -------------
Vorn und hinten Leerzeichen entfernen | Entfernt alle Leerzeichen (z. B. Leerzeichen, Tabulatoren) am Anfang und Ende des aktuellen Werts | ```value.trim()```
To titlecase| Konvertiert den aktuellen Wert in Großbuchstaben (d.h. jedes Wort beginnt mit einem Großbuchstaben und alle anderen Zeichen werden in Kleinbuchstaben umgewandelt) | ```value.toTitlecase()```
In Großbuchstaben| Wandelt den aktuellen Wert in Großbuchstaben um | ```value.toUppercase()```
In Kleinbuchstaben| Wandelt den aktuellen Wert in Kleinbuchstaben um | ```value.toLowercase()```

>## Publisher-Daten korrigieren
>1. Erstelle eine Textfacette für die Spalte "Publisher".
>2. beachte, dass es unter den Werten zwei gibt, die fast identisch aussehen - warum erscheinen diese beiden Werte getrennt und nicht als ein einziger Wert?
>3. wähle in der Verlagsspalte aus dem Dropdown-Menü die Option ``Edit cells->Common transforms->Collapse consecutive whitespace``.
>4. schau dir jetzt die Publisher-Facette an - hat sie sich geändert? (wenn sie sich nicht geändert hat, klicke auf die Option ``Aktualisieren``, um sicherzustellen, dass sie aktualisiert wird)
{: .checklist}
