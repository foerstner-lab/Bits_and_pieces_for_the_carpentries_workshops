---
Titel: "Einführung in OpenRefine"
Unterricht: 15
Übungen: 0
Fragen:
- "Was ist OpenRefine? Was kann es?"
Ziele:
- "Erkläre, was die OpenRefine-Software macht"
- "Erkläre, wie die OpenRefine-Software bei der Arbeit mit Datendateien helfen kann"
Kernpunkte:
- "OpenRefine ist 'ein Werkzeug für die Arbeit mit unordentlichen Daten'".
- "OpenRefine funktioniert am besten mit Daten in einem einfachen Tabellenformat".
- OpenRefine kann dir helfen, Daten in feinere Teile aufzuteilen.
- OpenRefine kann dir helfen, lokale Daten mit anderen Datensätzen abzugleichen.
- OpenRefine kann dir helfen, einen Datensatz mit Daten aus anderen Quellen anzureichern.
---

## Was ist OpenRefine?
OpenRefine ist eine Desktop-Anwendung, die deinen Webbrowser als grafische Oberfläche nutzt. 

OpenRefine ist am nützlichsten, wenn du Daten in einem einfachen Tabellenformat hast, z. B. in einer Tabellenkalkulation, einer csv oder tsv Datei. Mit OpenRefine kannst du die Daten in deiner Datei standardisieren und bereinigen. Es kann dir helfen:

* einen Überblick über einen Datensatz zu bekommen
* Unstimmigkeiten in einem Datensatz zu beseitigen, z. B. die Datumsformatierung zu standardisieren
* Daten in feinere Teile aufteilen, z.B. Zellen mit mehreren Autoren in separate Zellen aufteilen
* Abgleich lokaler Daten mit anderen Datensätzen - zum Beispiel beim Abgleich von Formen von Personennamen mit Namensautoritätsdatensätzen in der Virtual International Authority File (VIAF)
* Anreicherung eines Datensatzes mit Daten aus anderen Quellen

Einige häufige Szenarien könnten sein:

* Wenn du wissen willst, wie oft ein bestimmter Wert (Name, Verlag, Thema) in einer Spalte deiner Daten vorkommt
* Du möchtest wissen, wie die Werte über deinen gesamten Datensatz verteilt sind.
* Du hast eine Liste von Daten, die unterschiedlich formatiert sind, und möchtest alle Daten in der Liste in ein einheitliches Datumsformat ändern. Zum Beispiel:

| Daten, die du hast | Gewünschte Daten |
|-----------------|:-------------|
| 1. Januar 2014 | 2014-01-01 |
| 01/01/2014 | 2014-01-01 |
| 1. Januar 2014 | 2014-01-01 |
| 2014-01-01 | 2014-01-01 |

* Wenn du eine Liste von Namen oder Begriffen hast, die sich voneinander unterscheiden, sich aber auf die gleichen Personen, Orte oder Konzepte beziehen. Zum Beispiel:

| Daten, die du hast | Gewünschte Daten |
|-----------------|:-------------|
| London | London |
| London]         | London | London | London
| London,] | London | London |
| london | London | London |


* Wo du deine Daten aus einer externen Datenquelle ergänzen willst:

| Daten, die du hast | Geburtsdatum aus VIAF (Virtual International Authority File) | Sterbedatum aus VIAF (Virtual International Authority File) |
|-----------------|:-------------|:-------------|
| Braddon, M. E. (Mary Elizabeth) | 1835 | 1915 |
| Rossetti, William Michael | 1829 | 1919 |
| Prest, Thomas Peckett | 1810 | 1879 |

## Was sollte ich wissen, wenn ich mit OpenRefine arbeite?
* Es wird keine Internetverbindung benötigt und keine der Daten oder Befehle, die du in OpenRefine eingibst, werden an einen entfernten Server gesendet.
* Du änderst NICHT die Original-/Rohdaten.
* Die Projekte werden alle fünf Minuten und beim ordnungsgemäßen Beenden von OpenRefine (Strg+C) automatisch gespeichert. Siehe [Verlauf im Benutzerhandbuch] (https://docs.openrefine.org/manual/running/#history-undoredo) für weitere Informationen.
* Die Dateien werden lokal gespeichert, d. h., wenn du auf zwei Computern arbeitest, musst du Dateien/Projekte exportieren/importieren.
